"""
A set of decorators useful for building tests.  Stub keeps stub object types up
to date with the actual types.  It's used like this:

    class ActualType (object):
        ...
    
    @Stub(ActualClass)
    class StubType (object):
        ...
        
Now, if methods defined in the stub differ in signature from those defined in 
the original, an exception will be raised (currently at run time).

The patch decorator is similar, except that it acts on methods created on the
fly.  For example:

    class ActualType (object):
        def my_method(self, ...):
            ...
    
    inst = StubType()
    
    @patch(inst)
    def my_method(self, ...):
        ...

Now, if the signature of my_method gets out of sync with the one defined in 
ActualType, the test will raise an exception.  The patch decorator will also 
detect when it is working with stub instances:
    
    @Stub(ActualClass)
    class StubType (object):
        pass
    
    stub_inst = StubType()
    
    @patch(stub_inst)
    def my_method(self, ...):
        ...

"""
import inspect
import new

class StubException (Exception):
    pass

class Stub (object):
    """
    A decorator for creating a stub class
    """
    
    def __init__(self, real_cls):
        self.real_cls = real_cls
    
    def invalid_reason(self, stub_cls, member_name):
        """
        Return a reason that the given member is not valid in the given stub
        class.  If the member is valid, return None.
        """
        stub_member = getattr(stub_cls, member_name)
        stub_member_type = type(stub_member)
        while self.stubbed_type(stub_member_type) is not None:
            stub_member_type = self.stubbed_type(stub_member_type)
        
        # Fail if the real class does not have the member
        if not hasattr(self.real_cls, member_name):
            return '%s has no attribute %r' \
                % (self.real_cls.__name__, member_name)
        
        real_member = getattr(self.real_cls, member_name)
        real_member_type = type(real_member)
        
        # Fail if the types of the members differ
        if stub_member_type.__name__ != real_member_type.__name__:
            return 'Type mismatch for %s.%s' % (stub_cls.__name__, member_name)
        
        if stub_member_type.__name__ in ('instancemethod', 'function'):
            real_member_sig = inspect.getargspec(real_member)
            stub_member_sig = inspect.getargspec(stub_member)
            
            # Fail if they're functions with different signatures
            if real_member_sig != stub_member_sig:
                return 'Member functions have different signatures.'
        
        # Otherwise, pass
        return None
    
    def verify_stub_class(self, stub_cls):
        """
        Verify that the stub class is a valid stub for the real class.
        """
        real_members = dir(self.real_cls)
        stub_members = dir(stub_cls)
        
        for member_name in stub_members:
            invalid_reason = self.invalid_reason(stub_cls, member_name)
            if invalid_reason is not None:
                raise StubException('%s.%s is not a valid stub: %s' 
                    % (stub_cls.__name__, member_name, invalid_reason))
    
    def mark_as_stub_class(self, stub_cls):
        """
        Mark the given stub class as a stub of the real class.
        """
        stub_cls._stubbed_type = self.real_cls
    
    @staticmethod
    def stubbed_type(inst_or_cls):
        if hasattr(inst_or_cls, '_stubbed_type'):
            return inst_or_cls._stubbed_type
        
        return None
        
    def __call__(self, stub_cls):
        self.verify_stub_class(stub_cls)
        self.mark_as_stub_class(stub_cls)
        return stub_cls

class patch (object):
    """A decorator to patch the given instance with a function."""
    
    def __init__(self, instance):
        self.inst = instance
    
    def invalid_reason(self, inst_method):
        # Detect the type of inst, or the stubbed type.
        inst_type = Stub.stubbed_type(self.inst)
        if not inst_type:
            inst_type = type(self.inst)
        
        # If the type has no matching method name, fail.
        if not hasattr(inst_type, inst_method.__name__):
            return 'Instance %r does not have method %r' % (self.inst, inst_method.__name__)
        
        # If it has no matching method signature, fail.
        orig_method = getattr(inst_type, inst_method.__name__)
        
        orig_sig = inspect.getargspec(orig_method)
        inst_sig = inspect.getargspec(inst_method)
        
        if orig_sig != inst_sig:
            return 'Method signatures differ:\n %s\n %s' % (orig_sig,inst_sig)
        
        # Otherwise, pass.
        return None
        
    def verify_instance_patch(self, inst_method):
        """
        If an instance method with the same name as the new method exists on 
        the instance's type, and if the two methods have the same signatures,
        then all will be well.  If the instance's type was created with a Stub
        decorator, then this function will verify against the stubbed type.
        """
        inst_type = type(self.inst)
        
        invalid_reason = self.invalid_reason(inst_method)
        if invalid_reason is not None:
            raise StubException('%s is not a valid patch for %s: %s'
                % (inst_method.__name__, inst_type.__name__, invalid_reason))
    
    def __call__(self, method):
        inst_method = new.instancemethod(method, self.inst, self.inst.__class__)
        self.verify_instance_patch(inst_method)
        
        self.__name__ = method.__name__
        self.__doc__ = method.__doc__
        
        setattr(self.inst, inst_method.__name__, inst_method)
        return inst_method
        

#class Dec (object):
#    def __init__(self, f):
#        self.f = f
#        self.__name__ = f.__name__
#        self.__doc__ = f.__doc__
#    
#    def __call__(self, *args):
#        return f

#class A (object):
#    @Dec
#    def x(self):
#        pass

