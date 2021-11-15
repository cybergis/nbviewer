## Set the log level by value or name.
#  Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
#  Default: 30
c.Application.log_level = "DEBUG"

## Set the log level by value or name.
#  See also: Application.log_level
c.NBViewer.log_level = "DEBUG"


## Time to wait for a render to complete before showing the 'Working...' page.
#  Default: 15
c.NBViewer.render_timeout = 30


## Content-Security-Policy header setting.
#  Default: "connect-src 'none';"
c.NBViewer.content_security_policy = "connect-src http://localhost *.illinois.edu;"


## Number of threads to use for rendering.
#  Default: 1
c.NBViewer.threads = 8


## Minimum cache expiry (seconds).
#  Default: 600
# c.NBViewer.cache_expiry_min = 600


##### ------------------------------------------------------------------------
# Configuration file for NBViewer.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## This is an application.

## The date format used by logging formatters for %(asctime)s
#  Default: '%Y-%m-%d %H:%M:%S'
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  Default: '[%(name)s]%(highlevel)s %(message)s'
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
#  Default: 30
# c.Application.log_level = 30

## Instead of starting the Application, dump configuration to stdout
#  Default: False
# c.Application.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  Default: False
# c.Application.show_config_json = False

#------------------------------------------------------------------------------
# NBViewer(Application) configuration
#------------------------------------------------------------------------------
## This is an application.

## Answer yes to any questions (e.g. confirm overwrite).
#  Default: False
# c.NBViewer.answer_yes = False

## URL base for the server
#  Default: '/'
# c.NBViewer.base_url = '/'

## URL base for binder notebook execution service.
#  Default: 'https://mybinder.org/v2'
# c.NBViewer.binder_base_url = 'https://mybinder.org/v2'

## Maximum cache expiry (seconds).
#  Default: 7200
# c.NBViewer.cache_expiry_max = 7200

## Minimum cache expiry (seconds).
#  Default: 600
# c.NBViewer.cache_expiry_min = 600

#  Default: None
# c.NBViewer.client = None

## The config file to load.
#  Default: 'nbviewer_config.py'
# c.NBViewer.config_file = 'nbviewer_config.py'

## Content-Security-Policy header setting.
#  Default: "connect-src 'none';"
# c.NBViewer.content_security_policy = "connect-src 'none';"

## The Tornado handler to use for creation via frontpage form.
#  Default: 'nbviewer.handlers.CreateHandler'
# c.NBViewer.create_handler = 'nbviewer.handlers.CreateHandler'

## The Tornado handler to use for rendering 404 templates.
#  Default: 'nbviewer.handlers.Custom404'
# c.NBViewer.custom404_handler = 'nbviewer.handlers.Custom404'

## Format to use for legacy / URLs.
#  Default: 'html'
# c.NBViewer.default_format = 'html'

## The Tornado handler to use for rendering and viewing the FAQ section.
#  Default: 'nbviewer.handlers.FAQHandler'
# c.NBViewer.faq_handler = 'nbviewer.handlers.FAQHandler'

## Path to json file containing frontpage content.
#  Default: '/usr/local/lib/python3.7/site-packages/nbviewer/frontpage.json'
# c.NBViewer.frontpage = '/usr/local/lib/python3.7/site-packages/nbviewer/frontpage.json'

## Generate default config file.
#  Default: False
# c.NBViewer.generate_config = False

## The Tornado handler to use for viewing notebooks stored as GitHub Gists
#  Default: 'nbviewer.providers.gist.handlers.GistHandler'
# c.NBViewer.gist_handler = 'nbviewer.providers.gist.handlers.GistHandler'

## The Tornado handler to use for viewing notebooks stored as blobs on GitHub
#  Default: 'nbviewer.providers.github.handlers.GitHubBlobHandler'
# c.NBViewer.github_blob_handler = 'nbviewer.providers.github.handlers.GitHubBlobHandler'

## The Tornado handler to use for viewing directory trees on GitHub
#  Default: 'nbviewer.providers.github.handlers.GitHubTreeHandler'
# c.NBViewer.github_tree_handler = 'nbviewer.providers.github.handlers.GitHubTreeHandler'

## The Tornado handler to use for viewing all of a user's repositories on GitHub.
#  Default: 'nbviewer.providers.github.handlers.GitHubUserHandler'
# c.NBViewer.github_user_handler = 'nbviewer.providers.github.handlers.GitHubUserHandler'

#  Default: {}
# c.NBViewer.handler_settings = {}

## Run on the given interface.
#  Default: ''
# c.NBViewer.host = ''

#  Default: None
# c.NBViewer.index = None
## The Tornado handler to use for rendering the frontpage section.
#  Default: 'nbviewer.handlers.IndexHandler'
# c.NBViewer.index_handler = 'nbviewer.handlers.IndexHandler'

## URL base for ipywidgets JS package.
#  Default: 'https://unpkg.com/'
# c.NBViewer.ipywidgets_base_url = 'https://unpkg.com/'

## Version specifier for jupyter-js-widgets JS package.
#  Default: '*'
# c.NBViewer.jupyter_js_widgets_version = '*'

## Version specifier for @jupyter-widgets/html-manager JS package.
#  Default: '*'
# c.NBViewer.jupyter_widgets_html_manager_version = '*'

## The Tornado handler to use for viewing notebooks found on a local filesystem
#  Default: 'nbviewer.providers.local.handlers.LocalFileHandler'
# c.NBViewer.local_handler = 'nbviewer.providers.local.handlers.LocalFileHandler'

## Also serve files that are not readable by 'Other' on the local file system.
#  Default: False
# c.NBViewer.localfile_any_user = False

## Resolve/follow symbolic links to their target file using realpath.
#  Default: False
# c.NBViewer.localfile_follow_symlinks = False

## Allow to serve local files under /localfile/* this can be a security risk.
#  Default: ''
# c.NBViewer.localfiles = ''

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.NBViewer.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.NBViewer.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.NBViewer.log_level = "DEBUG"

## URL base for mathjax package.
#  Default: 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/'
# c.NBViewer.mathjax_url = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/'

#  Default: set()
# c.NBViewer.max_cache_uris = set()

## Number of threads to use for Async Memcache.
#  Default: 1
# c.NBViewer.mc_threads = 1

## Do not cache results.
#  Default: False
# c.NBViewer.no_cache = False

## Do not validate SSL certificates.
#  Default: False
# c.NBViewer.no_check_certificate = False

## Run on the given port.
#  Default: 0
# c.NBViewer.port = 0

## Use processes instead of threads for rendering.
#  Default: 0
# c.NBViewer.processes = 0

## Full dotted package(s) that provide `uri_rewrites`.
#  Default: ['nbviewer.providers.gist', 'nbviewer.providers.github', 'nbviewer.providers.dropbox', 'nbviewer.providers.url']
# c.NBViewer.provider_rewrites = ['nbviewer.providers.gist', 'nbviewer.providers.github', 'nbviewer.providers.dropbox', 'nbviewer.providers.url']

## Full dotted package(s) that provide `default_handlers`.
#  Default: ['nbviewer.providers.url', 'nbviewer.providers.github', 'nbviewer.providers.gist']
# c.NBViewer.providers = ['nbviewer.providers.url', 'nbviewer.providers.github', 'nbviewer.providers.gist']

## The proxy URL.
#  Default: ''
# c.NBViewer.proxy_host = ''

## The proxy port.
#  Default: -1
# c.NBViewer.proxy_port = -1

## Number of requests to allow in rate_limit_interval before limiting. Only
#  requests that trigger a new render are counted.
#  Default: 60
# c.NBViewer.rate_limit = 60

## Interval (in seconds) for rate limiting.
#  Default: 600
# c.NBViewer.rate_limit_interval = 600

## Time to wait for a render to complete before showing the 'Working...' page.
#  Default: 15
# c.NBViewer.render_timeout = 15

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.NBViewer.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.NBViewer.show_config_json = False

## Path to ssl .crt file.
#  Default: ''
# c.NBViewer.sslcert = ''

## Path to ssl .key file.
#  Default: ''
# c.NBViewer.sslkey = ''

## Custom path for loading additional static files.
#  Default: ''
# c.NBViewer.static_path = ''

#  Default: '/static/'
# c.NBViewer.static_url_prefix = '/static/'

## Host running statsd to send metrics to.
#  Default: ''
# c.NBViewer.statsd_host = ''

## Port on which statsd is listening for metrics on statsd_host.
#  Default: 8125
# c.NBViewer.statsd_port = 8125

## Prefix to use for naming metrics sent to statsd.
#  Default: 'nbviewer'
# c.NBViewer.statsd_prefix = 'nbviewer'

## Custom template path for the nbviewer app (not rendered notebooks).
#  Default: ''
# c.NBViewer.template_path = ''

## Number of threads to use for rendering.
#  Default: 1
# c.NBViewer.threads = 1

## The Tornado handler to use for viewing notebooks accessed via URL
#  Default: 'nbviewer.providers.url.handlers.URLHandler'
# c.NBViewer.url_handler = 'nbviewer.providers.url.handlers.URLHandler'

## The Tornado handler to use for viewing directory containing all of a user's
#  Gists
#  Default: 'nbviewer.providers.gist.handlers.UserGistsHandler'
# c.NBViewer.user_gists_handler = 'nbviewer.providers.gist.handlers.UserGistsHandler'

