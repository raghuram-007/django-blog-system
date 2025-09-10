from blog.models import Category
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help="data category insertion"
    
    def handle(self, *args, **options):
        categories=['Nature','Technology','Photography','Sports','Cars','Movie','Song','Health','Entertainment','News','Travel','Polictics','Space']
        for categorg in categories:
            Category.objects.create(name=categorg)
            self.stdout.write(self.style.SUCCESS("category is insertion completed"))
            