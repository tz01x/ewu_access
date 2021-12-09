from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.dispatch import receiver
import os,uuid
from .slugify import unique_slug_generator
from PIL import Image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from django.conf import settings
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys,os
import datetime

# Create your models here.
class ImageUploderPath():
    def __init__(self, img_upload_path) :
        self.img_upload_path = img_upload_path

    def uploadTo(self, instance, filename):
        base, ext = os.path.splitext(filename)
        filename = "%s.%s" % (uuid.uuid4(), ext[1:])
        return os.path.join(self.img_upload_path, filename)
    def uploadTo_withBasefile(self, instance, filename):
        base, ext = os.path.splitext(filename)
        filename = "%s_%s.%s" % (base,uuid.uuid4(), ext[1:])
        return os.path.join(self.img_upload_path, filename)
class Images(models.Model):

    picture=models.ImageField(upload_to=ImageUploderPath("images/").uploadTo,null=True,blank=True)
    # timage=models.ImageField(upload_to=ImageUploderPath("images/").uploadTo,null=True,blank=True)
    
    
    def save(self):
        # self.timage=self.picture
        # picture = Image.open(self.picture).convert("RGBA")
        # picture=picture.resize((1080,566))
        
        # make a blank image for the text, initialized to transparent text color
        # txt = Image.new('RGBA', picture.size, (255,255,255,0))

        # get a font
        # font = ImageFont.truetype(<font-file>, <font-size>)
        # font = ImageFont.truetype(os.path.join(settings.BASE_DIR,"./static/static_dir/font/Epilogue-BoldItalic.ttf"),60)
        # txt_width,txt_height=font.getsize('rental.bd.com')
        # draw = ImageDraw.Draw(txt)
        # print(picture.size)


        # # draw.text((x, y),"Sample Text",(r,g,b))
        # draw.text(((picture.width//2)-(txt_width//2), picture.height//2),"rental.bd.com","rgba(255,255,255,128)",font=font)
        # outimg = Image.alpha_composite(picture, txt)
        # outimg2=outimg.resize((256,256))
        # outimg=outimg.resize((1080,566))

        # output = BytesIO()
        # output2 = BytesIO()

        # #Resize/modify the image
        # # im = im.resize( (200,200) )


        
        # #filename , .jpg
        # # name, extension = os.path.splitext(self.picture.name)
        # # print(name,extension[1:])

        # #after modifications, save it to the output
        # outimg.save(output,'png', quality=32)
        # output.seek(0)
        # outimg2.save(output2,'png', quality=16)
        # output2.seek(0)
        # #change the imagefield value to be the newley modifed image value
        # imgname="img-%s%s"%(str(datetime.datetime.now().timestamp()).split('.')[0],'.png')
        # # print(imgname)
        # self.picture = InMemoryUploadedFile(output,'ImageField', imgname, 'png', sys.getsizeof(output), None)
        # self.timage = InMemoryUploadedFile(output2,'ImageField', imgname, 'png', sys.getsizeof(output2), None)

        super(Images,self).save()
    def delete(self, using=None, keep_parents=False):
       
        storage = self.picture.storage

        if storage.exists(self.picture.name):
            storage.delete(self.picture.name)

        # storage = self.timage.storage
        # if storage.exists(self.timage.name):
        #     storage.delete(self.timage.name)

        super().delete()


class Vote(models.Model):
    vtype=(("up","up"),("down","down"))
    created=models.DateTimeField(auto_now=True)
    voteType=models.CharField(max_length=4,choices=vtype)







class Comments(models.Model):

    user=models.ForeignKey(to=User,null=True,on_delete=models.SET_NULL)
    message=models.TextField(max_length=1000)
    replay=models.ManyToManyField(to='Comments')
    created=models.DateTimeField(auto_now=True)
    is_deleted=models.BooleanField(default=False)
    votes=models.ManyToManyField(to=Vote)
    def __str__(self):
        return self.message

    class Meta:
        verbose_name='Comment'

class Community(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    user=models.ForeignKey(to=User,on_delete=models.RESTRICT,related_name='communitys')
    slug=models.SlugField(max_length=11000, blank=True,null=True,unique=True,db_index=True,help_text='Don\'t need to fill this, because this field will be automaticaly ganarate')
    shortDescription = models.CharField(verbose_name='Short Description',max_length=1000)
    picture = models.ImageField(verbose_name='Picture', upload_to=ImageUploderPath(
        'community_profile/').uploadTo, null=True, blank=True)
    cover = models.ImageField(verbose_name='Picture', upload_to=ImageUploderPath(
        'community_cover/').uploadTo, null=True, blank=True)

    is_delete=models.BooleanField(default=False)
    is_public=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):

        pics = [self.picture,self.cover]

        for pic in pics:
            storage=pic.storage

            if storage.exists(pic.name):
                storage.delete(pic.name)

        super().delete()

@receiver(models.signals.pre_save, sender=Community)
def auto_slug_generator(sender, instance, **kwargs):
    """
    Creates a slug if there is no slug.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    slug=models.SlugField(max_length=11000, blank=True,null=True,unique=True,db_index=True,help_text='Don\'t need to fill this, because this field will be automaticaly ganarate')
    user=models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True,related_name='posts')
    community=models.ForeignKey(to=Community,on_delete=models.SET_NULL,null=True)
    
    is_delete=models.BooleanField(default=False)
    is_public=models.BooleanField(default=True)

    pictures=models.ManyToManyField(Images)

    comments=models.ManyToManyField(to=Comments)
    votes=models.ManyToManyField(to=Vote)

    def __str__(self) :
        return self.title




@receiver(models.signals.pre_save, sender=Post)
def auto_slug_generator(sender, instance, **kwargs):
    """
    Creates a slug if there is no slug.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)





    


    


