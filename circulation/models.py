from django.db import models
from accounts.models import User
from catalog.models import Book

class Loan(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('active', 'Active'),
        ('overdue', 'Overdue'),
        ('returned', 'Returned'),
    ]
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role__in': ['staff', 'admin']}, related_name='issued_loans')
    issued_on = models.DateField(auto_now_add=True)
    due_on = models.DateField()
    returned_on = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='requested')
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    class Meta:
        ordering = ['-issued_on']
    
    def __str__(self):
        return f"{self.member.username} - {self.book.title}"
