from blog.models import Media,Category

from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    
       
    help="insert the data"
    
    
   
        
    def handle(self, *args, **options):
      # Media.objects.all().delete
      
      title=[
        "The Beauty of Nature",
        "Disaster Field",
        "Artificial Take over",
        "Best of Photo",
        "Wildlife Scape",
        "Exploring the Tech World",

        "Daily Motivation Dose",
        
        "Travel Tales from the Hills",
        
        "Minimalism: A Way of Life",
        
        "Coding for Beginners: Tips & Tricks",
        
        "Mental Health Matters",
        
        "The Art of Storytelling",
        
        "Mastering Web Development",
        
        "Foodie Diaries: Taste Around the World"
        
    ]
      content=[
      " Nature has a way of bringing peace to our chaotic lives. The rustling of leaves, the chirping of birds, and the gentle touch of the breeze remind us to slow down and appreciate the world around us.",
      " Technology is evolving faster than ever before. From AI to blockchain, the digital landscape is constantly transforming. Staying updated with these trends is key for both professionals and enthusiasts alike. " ,
      "  Every morning is a new chance to start again. Whether it's a small win or a big breakthrough, progress is progress. Stay focused, stay positive, and keep moving forward.",
      " The mountains taught me patience. Each hike, each sunrise, and each local encounter added to the adventure. These memories now sit close to my heart, fueling my wanderlust.",
      "  Owning less and living more — that’s the core of minimalism. It's not about deprivation, but about making room for what truly matters.",
      "A structured morning routine can set the tone for your entire day. From meditation to journaling, just 30 minutes of mindfulness in the morning has helped me feel more focused, energized, and productive.",
      "Remote work isn't just a trend—it’s a shift in how we live and work. Flexible schedules, fewer commutes, and global collaboration are redefining what productivity looks like in 2025.",
      "From fiction to self-help, books have a way of opening our eyes to new ideas. Titles like Atomic Habits, Sapiens, and The Alchemist reshaped how I view personal growth, history, and purpose.",
      "Good design is invisible; great design is felt. Understanding user emotions, frustrations, and behaviors is key to crafting meaningful and intuitive digital experiences.",
      "Owning less and living more — that’s the core of minimalism. It's not about deprivation, but about making room for what truly matters.",
      "Owning less and living more — that’s the core of minimalism. It's not about deprivation, but about making room for what truly matters.",
    ]
      img=[
        "https://picsum.photos/id/128/200/300",
        "https://picsum.photos/id/36/200/300",
        "https://picsum.photos/id/1/200/300",
        
        
    ]
      
      categories=Category.objects.all()
      for title,content,img in zip(title,content,img):
        categer=random.choice(categories)
        Media.objects.create(title=title,content=content,img=img, categer=categer)
      self.stdout.write(self.style.SUCCESS("data insertion complete successfully"))
         
         
        
         
    