from instapy import InstaPy
import schedule

session = InstaPy(username='doineedavisadotorg', password='23wave25', headless_browser=True)

session.login()

def job():
	session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=14590,
                                    min_followers=100,
                                    min_following=100)

	session.set_do_follow(enabled=True, percentage=100, times=3)
	session.follow_by_tags(['travel', 'travelguide', 'architecture', 'digitalnomad', 'japan','travelphotography','europetravel', 'lisbon', 'iceland', 'travelgram'], amount=60)

	#Unfollow the users WHO do not follow you back:
	session.unfollow_users(amount=1000, nonFollowers=True, style="FIFO", unfollow_after=30, sleep_delay=5)


job()
schedule.every(6).hours.do(job)