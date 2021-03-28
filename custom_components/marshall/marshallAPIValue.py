"""Constants for the Marshall API values."""

# getting stuff
    
# GET_MULTIPLE, GET

SysMode = "netremote.sys.mode"    
SysInfoFriendlyname = "netremote.sys.info.friendlyname"
SysNetWlanMacaddress = "netremote.sys.net.wlan.macaddress"
SysInfoNetremotevendorid = "netremote.sys.info.netremotevendorid"
SysAudioVolume = "netremote.sys.audio.volume" #Can be set
SysCapsVolumesteps = "netremote.sys.caps.volumesteps"
SysAudioMute = "netremote.sys.audio.mute" #Can be set
SysAudioEqcustomParam0 = "netremote.sys.audio.eqcustom.param0" #Can be set
SysAudioEqcustomParam1 = "netremote.sys.audio.eqcustom.param1" #Can be set
SysPower = "netremote.sys.power"
SysInfoVersion = "netremote.sys.info.version"
MultiroomGroupMastervolume = "netremote.multiroom.group.mastervolume"
MultiroomDeviceClientindex = "netremote.multiroom.device.clientindex"
MultiroomDeviceListallversion = "netremote.multiroom.device.listallversion"
MultiroomGroupId = "netremote.multiroom.group.id"
MultiroomGroupName = "netremote.multiroom.group.name"
MultiroomGroupState = "netremote.multiroom.group.state"
PlatformOEMColorProduct = "netRemote.platform.OEM.colorProduct"
NavPresetCurrentpreset = "netremote.nav.preset.currentpreset"
PlayStatus = "netremote.play.status" # 0: Nothing while Bluetooth not connected / AUX 2: Playing  / or RCA  3: Paused while spotify 6: Stopped while streaming
PlayCaps = "netremote.play.caps"
PlayInfoDuration = "netremote.play.info.duration"
PlayInfoGraphicUri = "netremote.play.info.graphicuri"
PlayInfoArtist = "netremote.play.info.artist"
PlayInfoAlbum = "netremote.play.info.album"
PlayInfoName = "netremote.play.info.name"
PlayPosition = "netremote.play.position"
PlayShuffle = "netremote.play.shuffle"
PlayRepeat = "netremote.play.repeat"
SpotifyPlaylistName = "netremote.spotify.playlist.name"
SpotifyPlaylistUri = "netremote.spotify.playlist.uri"
    
    
# setting stuff & other
    
# LIST_GET_NEXT
    
# LIST_GET_NEXT/netremote.sys.caps.validmodes/-1?pin=1234&maxItems=20
# 0: Audsync 1: AUXIN 2: Airplay 3: Spotify 4: Google Cast 5: Bluetooth 6: IR 7: RCA 8: Standby 9: castsetup-default

    #  curl -v "http://192.168.2.121/fsapi/LIST_GET_NEXT/netremote.nav.presets/-1?pin=1234&maxItems=7"
    #  curl -v "http://192.168.2.116/fsapi/LIST_GET_NEXT/netremote.bluetooth.connecteddevices/-1?pin=1234&maxItems=20"
    #  curl -v "http://192.168.2.116/fsapi/LIST_GET_NEXT/netremote.multiroom.device.listall/-1?pin=1234&maxItems=20"
    #  curl -v "http://192.168.2.116/fsapi/LIST_GET_NEXT/netremote.sys.caps.validmodes/-1?pin=1234&maxItems=20"

    
NavPresets = "netremote.nav.presets"
BluetoothConnectedDevices = "netremote.bluetooth.connecteddevices"
MultiroomDeviceListall = "netremote.multiroom.device.listall"
SysCapsValidmodes = "netremote.sys.caps.validmodes"
    
    
# SET

NavActionSelectPreset = "netremote.nav.action.selectpreset" # seems to be counting up from 0
NavState = "netremote.nav.state" # 1 on selecting preset
PlayControl = "netremote.play.control" # 0: Play/Stop (on Radio) 2: Play/Pause (on Spotify) 3: Next 4: Prev
    
    
    #  curl -v "http://192.168.2.121/fsapi/CREATE_SESSION?pin=1234"
    #  curl -v "http://192.168.2.121/fsapi/GET_NOTIFIES?pin=1234&sid=527929965d"

