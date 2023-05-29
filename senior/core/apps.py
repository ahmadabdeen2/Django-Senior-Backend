from django.apps import AppConfig
from tensorflow.keras.models import load_model

def get_f1(y_true, y_pred):
    ...
    # compute F1 score
    return 1


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        self.keystroke_model = load_model('models/AYM_TRIAL_2.h5', custom_objects={'get_f1': get_f1})