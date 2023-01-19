from django.contrib import admin
from .models import Review


class Wordfilter(admin.SimpleListFilter):
    title = "Filter by words"

    # in URL
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class RatingGoodFilter(admin.SimpleListFilter):
    title = "Filter by Good(>=3) or Bad"
    parameter_name = "rating_good"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        choice = self.value()
        if choice == "good":
            return reviews.filter(payload__gte=3)
        elif choice == "bad":
            return reviews.filter(payload__lt=3)
        return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        Wordfilter,
        RatingGoodFilter,
        "rating",
        "room__pet_friendly",
    )
