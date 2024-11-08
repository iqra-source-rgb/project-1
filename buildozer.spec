[app]
title = Square
package.name = basicapp
package.domain = net.aesencryptornl
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3=3.10.12,kivy,pillow,hostpython3=3.10.12
version = 0.1
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[buildozer.android]
fullscreen = 0
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30.0.3
android.entrypoint = org.kivy.android.PythonActivity
android.manifest.theme = @android:style/Theme.NoTitleBar
android.update_sdk = True
android.javac_target = 1.8
android.accept_sdk_license = True  # Accepts the SDK license automatically

# Additional optional configurations
# android.build_tools_version = 30.0.3 # Uncomment if specifying build tools manually
# android.arch = armeabi-v7a,arm64-v8a # Specify architectures if needed
