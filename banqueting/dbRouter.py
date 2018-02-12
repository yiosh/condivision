class BanquetingRouter:
    """
    A router to control all database operations on models in the
    banqueting application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read banqueting models go to banqueting_db.
        """
        if model._meta.app_label == 'banqueting':
            return 'banqueting_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write banqueting models go to banqueting_db.
        """
        if model._meta.app_label == 'banqueting':
            return 'banqueting_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the banqueting app is involved.
        """
        if obj1._meta.app_label == 'banqueting' or \
           obj2._meta.app_label == 'banqueting':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the banqueting app only appears in the 'banqueting_db'
        database.
        """
        if app_label == 'banqueting':
            return db == 'banqueting_db'
        return None
