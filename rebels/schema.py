import graphene

from graphene_django.types import DjangoObjectType

from rebels.models import Ship, Rebel

class ShipType(DjangoObjectType):
    class Meta:
        model = Ship

class RebelType(DjangoObjectType):
    class Meta:
        model = Rebel

class RebelQuery:
    all_ships = graphene.List(ShipType, name=graphene.String())

    def resolve_all_ships(self, *args, name=None,**kwargs):
        if name:
            return Ship.objects.filter(name__icontains=name)
        return Ship.objects.all()
