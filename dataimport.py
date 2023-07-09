from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "すべあな界隈年表から全て歌詞の所為です。へデータをインポートする"

    def handle(self, *args, **options):
        print("hoge")