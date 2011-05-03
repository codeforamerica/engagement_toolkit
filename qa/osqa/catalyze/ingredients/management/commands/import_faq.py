from django.core.management.base import BaseCommand
from ingredients.management.faq import FaqDataFromCsv

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        username = args[0]
        csv_stream = open(args[1])
        
        faq_data = FaqDataFromCsv(csv_stream)
        faqs = faq_data.save(username)

