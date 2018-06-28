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
    all_ships = graphene.List(ShipType)

    def resolve_all_ships(self, *args, **kwargs):
        return Ship.objects.all()
