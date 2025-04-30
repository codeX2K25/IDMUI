from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.utils.database import init_db
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Import and register blueprints
    from app.routes import (
        auth, service_management, user_management,
        project_management, endpoint_management,
        domain_management, database_management,
        configuration_management, metrics,
        token_management, group_management
    )

    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(service_management.service_bp)
    app.register_blueprint(user_management.user_bp)
    app.register_blueprint(project_management.project_bp)
    app.register_blueprint(endpoint_management.endpoint_bp)
    app.register_blueprint(domain_management.domain_bp)
    app.register_blueprint(database_management.database_bp)
    app.register_blueprint(configuration_management.config_bp)
    app.register_blueprint(metrics.metrics_bp)
    app.register_blueprint(token_management.token_bp)
    app.register_blueprint(group_management.group_bp)

    with app.app_context():
        db.create_all()

        # Register custom Jinja filter for datetime formatting
        @app.template_filter('datetimeformat')
        def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
            if value is None:
                return ""
            return value.strftime(format)

    return app
