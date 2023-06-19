# Django import
from django.contrib.auth import get_user_model
# Third-Party import
from fcm_django.models import FCMDevice
from rest_framework import serializers
# Local import
from players.models import Player


class PlayerRecommendationNestedPlayer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'name', 'surname']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name', 'surname']




class PlayerRecommendationNestedUser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class PlayerRecommendationSerializer(serializers.Serializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    trainer = serializers.HyperlinkedRelatedField(view_name='user-detail',
                                                  lookup_field='id',
                                                  queryset=get_user_model().objects.all())

    player = serializers.HyperlinkedRelatedField(view_name='player-detail',
                                                 lookup_field='id',
                                                 queryset=Player.objects.all())

    class Meta:
        fields = ['owner', 'trainer', 'player']

    def send_notification(self):
        trainer = self.validated_data['trainer']
        player = self.validated_data['player']
        owner = self.validated_data['owner']

        request = self.context['request']
        trainer_serializer = PlayerRecommendationNestedUser(instance=trainer, context={'request': request})
        owner_serializer = PlayerRecommendationNestedUser(instance=owner, context={'request': request})
        player_serializer = PlayerRecommendationNestedPlayer(instance=player, context={'request': request})

        trainer_devices = FCMDevice.objects.filter(user=trainer).all()
        trainer_devices.send_message(title='Player Recommendation', data={
            'owner': owner_serializer.data,
            'trainer': trainer_serializer.data,
            'player': player_serializer.data,
        })



