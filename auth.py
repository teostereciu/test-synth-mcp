def authenticate(username, password):
    # TODO: Add validation
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return user
    return None
