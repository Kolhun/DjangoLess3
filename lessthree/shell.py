from task.models import Buyer

all_objects = Buyer.objects.all()
print(all_objects)

specific_object = Buyer.objects.get(id=1)
print(specific_object)

filtered_objects = Buyer.objects.filter(name="Test")
print(filtered_objects)

new_object = Buyer.objects.create(name="New Object", balance=100,   age=18)
print(new_object)

count = Buyer.objects.filter(name="Test").count()
print(count)
