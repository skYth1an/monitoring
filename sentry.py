import sentry_sdk
from sentry_sdk import capture_message
sentry_sdk.init(
    dsn="https://42a431c7fe7745858c08ac92e5ca9a6f@o1341132.ingest.sentry.io/6614281",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
a = int(input())
b = 0
c = a/b