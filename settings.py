from os import environ

SESSION_CONFIGS = [
    dict(
       name='VT_hoch',
       display_name="Video ACC",
       num_demo_participants=3,
       app_sequence=["instructions", "tasks", "peq"]
    ),
    dict(
       name='TT_hoch',
       display_name="Text ACC",
       num_demo_participants=3,
       app_sequence=["instructions", "tasks", "peq"]
    ),
    dict(
       name='UT_hoch',
       display_name="UNVideo AC",
       num_demo_participants=3,
       app_sequence=["instructions", "tasks", "peq"]
    ),
    dict(
       name='VT_niedrig',
       display_name="Video noACC",
       num_demo_participants=3,
       app_sequence=["instructions", "tasks", "peq"]
    ),
    dict(
       name='TT_niedrig',
       display_name="Text noACC",
       num_demo_participants=3,
       app_sequence=["instructions", "tasks", "peq"]
    ),
    dict(
       name='UT_niedrig',
       display_name="UNVideo noACC",
       num_demo_participants=3,
       app_sequence=["instructions", "tasks", "peq"]
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=3.75, doc=""
),
dict(
    keywords='bonus, study',
    title='Title for your experiment',
    description='Description for your experiment',
    frame_height=500,
    template='global/mturk_template.html',
    minutes_allotted_per_assignment=60,
    expiration_hours=7 * 24,
    qualification_requirements=[]
    # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5pug1m_y2pz7#&0dr(s@k*#whs8=3@#cfyzj%in%n6k1woe_m-'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

