from django.db import models


# class Video(models.Model):
#     id = models.CharField(max_length=20, primary_key=True)
#     url = models.URLField()
#     title = models.CharField(max_length=255)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.id = self.get_video_id()
#         super().save(*args, **kwargs)

#     def get_video_id(self):
#         # Extract the video ID from the YouTube URL
#         video_id = self.url.split("v=")[1]
#         return video_id


# class Streams(models.Model):
#     video_id = models.ForeignKey(
#         Video, on_delete=models.CASCADE, related_name='streams')
#     resolution = models.CharField(max_length=50)
#     download_link = models.URLField(blank=True)
