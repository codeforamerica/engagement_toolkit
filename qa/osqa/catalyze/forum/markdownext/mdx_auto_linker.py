import markdown
import re, socket

TLDS = ('gw', 'gu', 'gt', 'gs', 'gr', 'gq', 'gp', 'gy', 'gg', 'gf', 'ge', 'gd', 'ga', 'edu', 'va', 'gn', 'gl', 'gi',
        'gh', 'iq', 'lb', 'lc', 'la', 'tv', 'tw', 'tt', 'arpa', 'lk', 'li', 'lv', 'to', 'lt', 'lr', 'ls', 'th', 'tf',
        'su', 'td', 'aspx', 'tc', 'ly', 'do', 'coop', 'dj', 'dk', 'de', 'vc', 'me', 'dz', 'uy', 'yu', 'vg', 'ro',
        'vu', 'qa', 'ml', 'us', 'zm', 'cfm', 'tel', 'ee', 'htm', 'za', 'ec', 'bg', 'uk', 'eu', 'et', 'zw',
        'es', 'er', 'ru', 'rw', 'rs', 'asia', 're', 'it', 'net', 'gov', 'tz', 'bd', 'be', 'bf', 'asp', 'jobs', 'ba',
        'bb', 'bm', 'bn', 'bo', 'bh', 'bi', 'bj', 'bt', 'jm', 'sb', 'bw', 'ws', 'br', 'bs', 'je', 'tg', 'by', 'bz',
        'tn', 'om', 'ua', 'jo', 'pdf', 'mz', 'com', 'ck', 'ci', 'ch', 'co', 'cn', 'cm', 'cl', 'cc', 'tr', 'ca', 'cg',
        'cf', 'cd', 'cz', 'cy', 'cx', 'org', 'cr', 'txt', 'cv', 'cu', 've', 'pr', 'ps', 'fk', 'pw', 'pt', 'museum',
        'py', 'tl', 'int', 'pa', 'pf', 'pg', 'pe', 'pk', 'ph', 'pn', 'eg', 'pl', 'tk', 'hr', 'aero', 'ht', 'hu', 'hk',
        'hn', 'vn', 'hm', 'jp', 'info', 'md', 'mg', 'ma', 'mc', 'uz', 'mm', 'local', 'mo', 'mn', 'mh', 'mk', 'cat',
        'mu', 'mt', 'mw', 'mv', 'mq', 'ms', 'mr', 'im', 'ug', 'my', 'mx', 'il', 'pro', 'ac', 'sa', 'ae', 'ad', 'ag',
        'af', 'ai', 'vi', 'is', 'ir', 'am', 'al', 'ao', 'an', 'aq', 'as', 'ar', 'au', 'at', 'aw', 'in', 'ax', 'az',
        'ie', 'id', 'sr', 'nl', 'mil', 'no', 'na', 'travel', 'nc', 'ne', 'nf', 'ng', 'nz', 'dm', 'np',
        'so', 'nr', 'nu', 'fr', 'io', 'ni', 'ye', 'sv', 'jsp', 'kz', 'fi', 'fj', 'php', 'fm', 'fo', 'tj', 'sz', 'sy',
        'mobi', 'kg', 'ke', 'doc', 'ki', 'kh', 'kn', 'km', 'st', 'sk', 'kr', 'si', 'kp', 'kw', 'sn', 'sm', 'sl', 'sc',
        'biz', 'ky', 'sg', 'se', 'sd')

AUTO_LINK_RE = re.compile(r"""
    (?P<ws>.?\s*)
    (?P<url>
        (?:(?P<format1>
            ((?P<protocol1>[a-z][a-z]+)://)?
            (?P<domain1>\w(?:[\w-]*\w)?\.\w(?:[\w-]*\w)?(?:\.\w(?:[\w-]*\w)?)*)
        ) | (?P<format2>
            ((?P<protocol2>[a-z][a-z]+)://)
            (?P<domain2>\w(?:[\w-]*\w)?(?:\.\w(?:[\w-]*\w)?)*)
        ))
        (?P<port>:\d+)?
        (?P<uri>/[^\s<]*)?
    )

""", re.X | re.I)

def is_ip(addr):
    try:
        socket.inet_aton(addr)
        return True
    except:
        return False

def replacer(m):

    ws = m.group('ws')

    if ws and ws[0] in ("'", '"'):
        return m.group(0)

    elif not ws:
        ws = ''

    if m.group('format1'):
        fn = 1
    else:
        fn = 2

    protocol = m.group('protocol%s' % fn)
    domain = m.group('domain%s' % fn)

    if not protocol:
        domain_chunks = domain.split('.')

        if not ((len(domain_chunks) == 1 and domain_chunks[0].lower() == 'localhost') or (domain_chunks[-1].lower() in TLDS)):
            return m.group(0)

    if (not protocol) and is_ip(domain):
        return m.group(0)


    port = m.group('port')
    uri = m.group('uri')

    if not ws:
        ws = ''

    if not port:
        port = ''

    if not protocol:
        protocol = 'http'

    if not uri:
        uri = ''

    url = "%s://%s%s%s" % (protocol, domain, port, uri)

    return "%s<a href=\"%s\">%s</a>" % (ws, url, m.group('url'))


class AutoLinker(markdown.postprocessors.Postprocessor):

    def run(self, text):
        return AUTO_LINK_RE.sub(replacer, text)

class AutoLinkerExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors['autolinker'] = AutoLinker()

def makeExtension(configs=None):
    return AutoLinkerExtension(configs=configs)


