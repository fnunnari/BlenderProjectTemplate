'''Application Data (bpy.app)
   This module contains application values that remain unchanged during runtime.
   Submodules:
   .. toctree::
   :maxdepth: 1
   bpy.app.handlers.rst
   bpy.app.icons.rst
   bpy.app.timers.rst
   bpy.app.translations.rst
   
'''


autoexec_fail = None



autoexec_fail_message = None



autoexec_fail_quiet = None



binary_path_python = None
'''String, the path to the python executable (read-only)
   
'''


debug = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_depsgraph = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_depsgraph_build = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_depsgraph_eval = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_depsgraph_pretty = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_depsgraph_tag = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_depsgraph_time = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_events = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_ffmpeg = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_freestyle = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_gpumem = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_handlers = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_io = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_python = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_simdata = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


debug_value = None
'''Short, number which can be set to non-zero values for testing purposes
   
'''


debug_wm = None
'''Boolean, for debug info (started with --debug / --debug_* matching this attribute name)
   
'''


driver_namespace = None
'''Dictionary for drivers namespace, editable in-place, reset on file load (read-only)
   
'''


render_icon_size = None
'''Reference size for icon/preview renders (read-only)
   
'''


render_preview_size = None
'''Reference size for icon/preview renders (read-only)
   
'''


tempdir = None
'''String, the temp directory used by blender (read-only)
   
'''


use_event_simulate = None
'''Boolean, for application behavior (started with --enable-* matching this attribute name)
   
'''


use_override_library = None
'''Boolean, whether library override is exposed in UI or not.
   
'''


use_userpref_skip_save_on_exit = None
'''Boolean, for application behavior (started with --enable-* matching this attribute name)
   
'''


alembic = None
'''Alembic library information backend
   
'''


background = None
'''Boolean, True when blender is running without a user interface (started with -b)
   
'''


binary_path = None
'''The location of Blender's executable, useful for utilities that open new instances
   
'''


build_branch = None
'''The branch this blender instance was built from
   
'''


build_cflags = None
'''C compiler flags
   
'''


build_commit_date = None
'''The date of commit this blender instance was built
   
'''


build_commit_time = None
'''The time of commit this blender instance was built
   
'''


build_commit_timestamp = None
'''The unix timestamp of commit this blender instance was built
   
'''


build_cxxflags = None
'''C++ compiler flags
   
'''


build_date = None
'''The date this blender instance was built
   
'''


build_hash = None
'''The commit hash this blender instance was built with
   
'''


build_linkflags = None
'''Binary linking flags
   
'''


build_options = None
'''A set containing most important enabled optional build features
   
'''


build_platform = None
'''The platform this blender instance was built for
   
'''


build_system = None
'''Build system used
   
'''


build_time = None
'''The time this blender instance was built
   
'''


build_type = None
'''The type of build (Release, Debug)
   
'''


factory_startup = None
'''Boolean, True when blender is running with --factory-startup)
   
'''


ffmpeg = None
'''FFmpeg library information backend
   
'''


handlers = None
'''Application handler callbacks
   
'''


icons = None
'''Manage custom icons
   
'''


ocio = None
'''OpenColorIO library information backend
   
'''


oiio = None
'''OpenImageIO library information backend
   
'''


opensubdiv = None
'''OpenSubdiv library information backend
   
'''


openvdb = None
'''OpenVDB library information backend
   
'''


sdl = None
'''SDL library information backend
   
'''


timers = None
'''Manage timers
   
'''


translations = None
'''Application and addons internationalization API
   
'''


usd = None
'''USD library information backend
   
'''


version = None
'''The Blender version as a tuple of 3 numbers. eg. (2, 83, 1)
   
'''


version_char = None
'''Deprecated, always an empty string
   
'''


version_cycle = None
'''The release status of this build alpha/beta/rc/release
   
'''


version_string = None
'''The Blender version formatted as a string
   
'''


def count(*argv):
   '''Return number of occurrences of value.
      
   '''

   pass

def index(*argv):
   '''Return first index of value.
      Raises ValueError if the value is not present.
      
   '''

   pass

