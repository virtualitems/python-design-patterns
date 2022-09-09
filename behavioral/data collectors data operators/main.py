"""
código cliente
"""

from collectors import list_all_users, list_users_without_subscription
from operators import send_gift, send_ad

if __name__ == "__main__":

    print('\nSENDING AD')
    users = list_all_users()
    send_ad(users)

    print('\nSENDING GIFT')
    users = list_users_without_subscription()
    send_gift(users)
