from django.db import models

class Bags(models.Model):
    recorded = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(null=True)
    purchased = models.PositiveIntegerField(null=True)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

    def _consumed(self):
        if self.id == 1:
            consumed = 0
        else:
            prev = self.get_previous_by_recorded()

            if self.purchased:
                oldcount = prev.count + self.purchased
            else:
                oldcount = prev.count

            consumed = oldcount - self.count
            # consumed = self.purchased

        return consumed


    consumed = property(_consumed)
class Hopper(models.Model):
    recorded = models.DateTimeField(auto_now_add=True)
    level = models.PositiveIntegerField()

    def _consumed(self):
        if self.id == 1:
            consumed = 0
        else:
            prev = self.get_previous_by_recorded()
            if prev.level < self.level:
                consumed = 0
            else:
                consumed = prev.level - self.level

        return consumed


    consumed = property(_consumed)


    def _get_full_name(self):
        "Returns the person's full name."
        return '%s, %s %s' % (self.lastname, self.firstname, self.middlename)
    full_name = property(_get_full_name)
