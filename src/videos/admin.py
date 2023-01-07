from django.contrib import admin

from .models import VideoAllProxy, VideoPublishedProxy

class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id', 'state', 'is_published']
    search_fields = ['title']
    list_filter = ['active', 'state']
    readonly_fields = ['id', 'is_published', 'publish_timestamp']
    class Meta:
        model = VideoAllProxy

class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoAllProxy, VideoAllAdmin)


admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
