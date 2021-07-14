from django.db import models


class Friend(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Belonging(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Borrowed(models.Model):
	what_thing = models.ForeignKey(Belonging, on_delete=models.CASCADE)
	to_whom = models.ForeignKey(Friend, on_delete=models.CASCADE)
	when = models.DateTimeField(auto_now_add=True)
	returned_when = models.DateTimeField(null=True, blank=True)

	class Meta:
		verbose_name_plural = "Borrowed Items"

	def __str__(self):
		return f"{self.what_thing} was borrowed by {self.to_whom} on {self.when}"