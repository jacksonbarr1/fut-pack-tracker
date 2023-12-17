from django.db import models

class Pack(models.Model):
    pack_id = models.IntegerField(primary_key=True, auto_created=False)
    pack_name = models.CharField(max_length=64)
    coin_value = models.IntegerField()
    fcp_value = models.IntegerField()
    item_count = models.IntegerField()
    rare_item_count = models.IntegerField()
    player_count = models.IntegerField()

    def __str__(self):
        return self.pack_name

    # Override to ensure no rows are created/updated from static db
    def save(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
