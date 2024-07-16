from models import User, Order
from main import Session

# with Session() as session:
#     new_user = User(username='john doe', email='john@example.com')
#     session.add(new_user)
#     session.commit()

# with Session() as session:
#     users = session.query(User).all()
#     for user in users:
#         print(user.username, user.email)

# with Session() as session:
#     user_to_update = session.query(User).filter_by(username='john doe').first()
#
#     if user_to_update:
#         user_to_update.email = 'new_email@example.com'
#         session.commit()
#         print('User updated successfully')
#     else:
#         print('User not found')


# session = Session()

# try:
#     session.begin()
#     session.query(User).delete()
#     session.commit()
#     print('All users deleted successfully')
# except Exception as e:
#     session.rollback()
#     print(f'Error occurred {str(e)}')
# finally:
#     session.close()

# new_users = [
#     User(username='john_doe', email='john.doe@example.com'),
#     User(username='sarah_smith', email='sarah.smith@gmail.com'),
#     User(username='mike_jones', email='mike.jones@company.com'),
#     User(username='emma_wilson', email='emma.wilson@domain.net'),
#     User(username='david_brown', email='david.brown@email.org')
# ]
#
# session.begin()
# session.add_all(new_users)
# session.commit()
# session.close()

# with Session() as session:
#     session.add_all((Order(user_id=8), Order(user_id=10)))
#     session.commit()

with Session() as session:
    orders = session.query(Order).order_by(Order.user_id.desc()).all()

    if not orders:
        print('No orders yet')
    else:
        for order in orders:
            user = order.user
            print(f"Order number {order.id}, Is completed: {order.is_completed}, Username: {user.username}")