# Restoring a session
class SessionManager:
    def restore_session(self):
        try:
            with open(SESSION_FILE, 'rb') as f:
                session = pickle.load(f)
                self.validate_session(session)
                return session
        except Exception as e:
            self.logger.error(f"Recovery error: {str(e)}")
            return self.create_new_session()

    def validate_session(self, session):
        if session.balance != get_exchange_balance():
            raise InvalidSessionError("The balance does not match the exchange")
