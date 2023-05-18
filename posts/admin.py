from django.contrib import admin

from .models import Tweet, Reaction, ReactionType, TweetImages, Reply


@admin.display(description='Short text')
def get_short_text(obj):
    return f'{obj.text[:10]}...'
#
# class TweetAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Tweet, TweetAdmin)


class TweetImagesInline(admin.TabularInline):
    model = TweetImages
    extra = 1


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    inlines = [
        TweetImagesInline
    ]
    date_hierarchy = 'created_at'
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = '--empty--'
    # exclude = ['profile', 'image']
    # fields = ['text', ]
    fields = (('text', 'profile'), 'image')
    list_display = ['id', 'get_profile_fullname', get_short_text, 'get_reactions_str', 'image', 'created_at', 'profile']
    list_display_links = [get_short_text, 'id']
    list_editable = ['image', ]
    list_filter = ['created_at', 'profile']
    list_per_page = 2
    save_as = True
    save_on_top = True
    search_fields = ['text', 'profile__user__username__exact']
    sortable_by = ['created_at', 'id']

    @admin.display(description='fullname')
    def get_profile_fullname(self, obj):
        return obj.profile.user.get_full_name()


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    pass


@admin.register(ReactionType)
class ReactionType(admin.ModelAdmin):
    pass


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['tweet' , get_short_text, 'created_at', 'updated_at', 'profile', 'get_reactions_str']
    search_fields = ['text', 'profile__user__username__exact']
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = '-'
    fields = (('text', 'profile'), 'tweet')
    list_editable = ['profile', ]
    sortable_by = ['created_at', 'id']
