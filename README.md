# Tablet VR
Controller for virtual reality tasks for execution of arbitrary experimental paradigms. The virtual environments (aka scenes) are displayed in several monitor tablets around the field of view of the subject.

## Prerequisites
* [Unity 3D][Unity 3D]
* [Android Studio][Android Studio] (Optional)
* [Java SDK][Java SDK] (Optional)
* Port UDP 32000 enabled in the firewall/network for Unity, and any compilation.

Code was last built and tested with
* Unity 2019.3.15f1
* Android Studio 3.1.2
	* Android SDK Platform 27 revision 3
	* Android SDK Build-Tools 28-rc2 version 28.0.0 rc2
* Tablets
	* OS: Android 5.0
	* SoC: Qualcomm Snapdragon 410 APQ8016

## Installation
* Install Android Studio.
* Install Unity, adding support for Android.
* Open Unity and load the project folder.
	
## Testing scenes in Unity
* Open `Main` scene and hit play.

## Deployment
* Add scenes to build settings.
* Open Main scene.
* Build for Android.
* Run TabletVR.apk in each tablet.

## Contributions
Original [repo](https://github.com/leomol/SmoothWalk/tree/master?tab=GPL-3.0-1-ov-file) (I didn't fork, because I want commits :])

[Java SDK]: http://www.oracle.com/technetwork/java/javase/downloads/index.html
[Unity 3D]: https://unity3d.com/unity
[Android Studio]: https://developer.android.com/studio
