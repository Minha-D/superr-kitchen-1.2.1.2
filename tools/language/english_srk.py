# -*- coding: utf-8 -*-

# Main Menu
title_main = "Main Menu"
title_choose = "Choose project:"
title_delete = "Delete Projects:"
title_extract = "Extract Options:"
menu_create = "Create new project"
menu_choose = "Choose a different project"
menu_delete = "Delete a project"
menu_extract = "Extract for new ROM"
menu_updates = "Check for updates"
menu_misc = "Misc Tools"
menu_boot_recovery = "Boot/Recovery Tools"
menu_rom_tools = "ROM Tools Menu"
menu_new = "New Project"
menu_quit = "Quit"
menu_back = "Back"
menu_skip = "Skip"

# ROM Tools Menu
menu_deodex = "Deodex ROM "
menu_perm_type = "Change perm type "
menu_root = "Root Menu"
menu_asserts = "Asserts Menu"
menu_extra_dir = "Extra Directory Menu"
menu_rom_debloat = "Debloat Menu"
menu_build_menu = "Build Menu"

# Startup
startup_project = "CURRENT PROJECT: "
startup_version = "ANDROID VERSION: "
startup_mdepend = "MISSING DEPENDENCY: "
startup_need_java = "You need at least Java 8 to use this kitchen."
startup_copy_extract = "Copy your firmware to the project"
startup_copy_extract2 = "directory and choose option 4 to extract it."
startup_title_no_rom = "No ROM"
startup_no_projects = "There is no project to work on."
startup_prep_updater_script = "Preparing updater-script ..."
startup_no_rom = "There is no ROM to work on."
startup_srkuser = "Enter your Kitchen username (not email):"
startup_srkuser_pass = "Kitchen Password: "
startup_srkuser_error = "Do not enter your email, only the username."
startup_srkuser_error2 = " was not found in the kitchen database OR"
startup_srkuser_error3 = "the password was incorrect. Make sure you type"
startup_srkuser_error4 = "the username/password you entered when you"
startup_srkuser_error5 = "registered for the kitchen."
startup_srkuser_noauth = "This PC is not authorized."
startup_srkuser_unknown = "An unknown error occured. Please contact SuperR."
startup_srkuser_q = "Is this your kitchen username?  y/n"
startup_srkpass_q = "Would you like to save your password?  y/n"
startup_error = "Something is wrong with your install. Try a fresh install."
startup_checksum = "The following checksums did not match:"
startup_environ_error = "The kitchen can't run in this environment"
startup_vdisk_error = "The kitchen can't run on a virtual disk in Live mode"
startup_remdisk_error = "The kitchen can't run on a removable disk in Live mode"
startup_wsl_warning = "You are running the kitchen in WSL1."
startup_wsl_warning2 = "WSL2 is recommended to enable the full capabilities of the kitchen."
startup_wsl2_warning = "The kitchen is not running in the /home directory."
startup_wsl2_warning2 = "This may cause Windows permissions errors and general slowness."
startup_win_warning = "The native Windows kitchen is being phased out."
startup_win_warning2 = "WSL2 is the perfect way to run the Linux kitchen in Windows."

# Build
menu_build_zip = "Build full ROM Zip"
menu_sys_img = "Build EXT4 img"
menu_sign = "Sign existing zip"
donate_menu_zipalign = "Zipalign apk files"
donate_menu_custom_id = "Custom ro.build.display.id"
menu_custom_zip = "Custom zip menu"
build_selinux_error = "Either your kernel does not support selinux, or the"
build_selinux_error2 = "kitchen can't find what it needs. If you are sure your"
build_selinux_error3 = "device supports selinux, you can copy the file_contexts"
build_selinux_error4 = "file from the ramdisk to your 00_project_files directory"
build_selinux_error5 = "to use this feature."
build_selinux_error6 = "For now, you will need to use set_perm or raw_img."
build_patient = "This may take a while. Please be patient ..."
build_prep_img = "Preparing files for img creation ..."
build_check_ziplog = "Something went wrong. Check the zip.log for errors."
build_prep_sys_img = "Preparing files for EXT4 img creation ..."
build_img_error = "There was a problem creating the image."
build_img_which = "Which EXT4 img would you like to build?"
build_img_nocon = "The kitchen did not find the file_contexts file. Make"
build_img_nocon2 = "sure the boot.img is in your project directory, or copy"
build_img_nocon3 = "file_contexts into your project 00_project_files directory"
build_img_nocon4 = "and try again."
build_no_zip = "There is no zip to sign."
build_no_boot_q = "Your ROM does not contain a boot.img or kernel.img/ramdisk.img."
build_no_boot_q2 = "Would you like to continue anyway?  y/n"
build_cho_zip = "Choose zip to sign:"
build_man_img_size = "Would you like to use the following size?  y/n"
zipalign_q = "Should we zipalign before building the zip?  y/n  "
zipalign = "Zipaligning"
zipalign_frame_q = "Would you also like to zipalign the apk files in /framework?  y/n  "
zipalign_complete = "Zipalign complete"
donate_bdisplay = "What would you like your build display to say?"

# Custom zip
title_cho_cust_zip = "Choose custom zip to build:"
cust_deldir_q = "Would you like the zip to delete the existing"
cust_deldir_q2 = "directories before flashing?  y/n"
cust_meta_prep = "Preparing META-INF directory ..."
cust_not_exist = "One or more directories you want to zip do not exist."
cust_dir_info = "Make sure you have at least one of the following in "
cust_file_check = "Make sure you have system, META-INF, and boot.img in "
cust_prep = "Preparing files ..."
cust_convert_binary_q = "Would you like to convert your updater-script"
cust_convert_binary_q2 = "to an update-binary?  y/n  "
cust_convert_binary = "Converting updater-script to update-binary ..."

# Debloat
menu_debloat = "Debloat ROM"
menu_debloat_cust = "Custom Debloat"
menu_debloat_knox = "Remove Samsung Knox"
menu_debloat_restore = "Restore Bloat/Knox"
menu_debloat_refresh = "Refresh Bloat Status"
bloat_already_debloated = "This ROM is already debloated"
bloat_list_menu = "List files that will be removed"
bloat_list_files = "The following files will be removed:"
bloat_rem = "Removing bloat ..."
bloat_moved = "Bloat has been moved to:"
bloat_cust_info = "Add content to one of the following files to use this feature"
bloat_knox_not_exist = "Knox is not present in this ROM"
bloat_knox_rem = "Removing knox ..."
bloat_knox_moved = "Knox has been moved to:"
bloat_no_files_restore = "There are no files to restore"
bloat_restore = "Restoring bloat ..."
bloat_has_restored = "The bloat has been restored."
bloat_restore_q = "Would you like to restore bloat?  y/n  "
debloated = "Debloated"
bloated = "Bloated"
bloat_dir_emply = "bloat_custom is EMPTY"

# Root
title_cho_root_zip = "Choose Root Zip:"
menu_root_method = "Which root method would you like?"
menu_ss_method = "What type of SuperSU install would you like?"
menu_supersucho = "Let SuperSU decide"
menu_system_install = "System install (SYSTEMLESS = false)"
menu_inject = "Inject sepolicy changes and system install"
menu_download_inject = "Download/Install inject-sepolicy-addon"
menu_root_unroot = "Root/Unroot ROM"
menu_busybox = "Busybox Add/Remove"
menu_add_remove_sud = "Add/Remove su.d support"
root_already = "You already have root."
root_must_add = "You must add root first."
busybox_already = "You already have Busybox."
busybox_q = "Should we add Busybox to the ROM?  y/n  "
root_sud_add_q = "Would you like to add su.d to your rom?  y/n  "
root_sud_rem_q = "Would you like to remove su.d support?  y/n  "
root_supersu_q = "SuperSU is a dead project. Are you sure you want to add it?  y/n"
root_remove = "Removing root ..."

# General
general_remove_q = "Should we remove it?  y/n  "
general_continue_q = "Would you like to continue?  y/n  "
general_cont_anyway_q = "Would you like to continue anyway?  y/n  "
general_extracting = "Extracting "
general_create = "has been created in "
general_build = "is building in "
no_python = "You must install Python3.5 or higher to use this feature."
more_info_link = "Visit the following link for more information:"
spaces_not_allowed = "Spaces are not allowed"

# Status
enabled = "Enabled"
disabled = "Disabled"
add_support = "Add Support"
yes = "Yes"
no = "No"
secure = "Secure"
insecure = "Insecure"
no_knox = "No Knox"
knox = "Knox exists"
no_root = "No Root"

# Boot/Recovery Tools
title_boot = "Boot/Recovery Tools Menu"
title_cho_boot = "Choose boot or recovery img"
title_unpack = "Unpack for more options"
title_current = "CURRENT: "
menu_pack_boot = "Pack "
menu_insecure = "Insecure/Secure the "
menu_dmverity = "Remove dm-verity"
menu_forcee = "Add/Remove forceencrypt"
menu_deopatch = "Patch sepolicy for Oreo deodex"
menu_deopatch_fail = "Patch failed, or sepolicy has already been patched"
menu_deopatch_sepol = "sepolicy was not found"
menu_deopatch_add = "sepolicy has been patched for Oreo deodex"
menu_unpack = "Unpack "
menu_boot_flashable = "Build flashable "
menu_boot_restore = "Restore to original: "
menu_switch_boot = "Switch between boot/recovery"
boot_repack = "Repacking "
boot_repack_problem = "There was a problem repacking your"
boot_packed_d = " packed"
boot_no_img = "There is no boot.img or recovery.img in "
boot_prop_warn = "Please copy a build.prop to the project directory and try again."
boot_prep_build = "Preparing to build ..."
boot_unpack = "Unpacking "
boot_unpack_problem = "There was a problem unpacking your "
boot_unpack_noram = "There is no ramdisk in this boot.img."
boot_need_img = "You need an img for this process."
boot_permission_error = "There is a permissions error. Check the boot.log"
boot_permission_error2 = "This post provides solutions:"

# Plugin Manager
menu_plugin_menu = "Plugin Manager"
menu_plugin_run = "Run a plugin"
menu_plugin_install = "Install a plugin"
menu_plugin_delete = "Delete a plugin"
menu_plugin_updates = "Check for plugin updates"
menu_plugin_updates_info = "Updates available:"
menu_plugin_get = "Getting plugin list ..."
menu_plugin_bashwin = "You can't run Bash plugins in Windows. Use the"
menu_plugin_bashwin2 = "plugin manager to delete and reinstall the correct version."

# Misc Tools Menu
title_misc = "Misc Tools Menu"
menu_language = "Reset language"
menu_heapsize = "Heapsize Menu"
menu_support = "Support: Create zip to send"
menu_zip_devices = "Zip devices/capfiles to share"
menu_ubinary = "update-binary zip options"
menu_flashable = "Flashable zip options (global)"
menu_extract_options = "Extract Options"
menu_mount_extract = "Use mount extract for img files"
menu_case_fix = "Case insensitive file names fix"
menu_extract_all_img = "Extract and include all img files"
menu_tools_reset = "Reset all tools"
menu_tools_reset_go = "Removing all tools ..."
menu_device_reset = "Update device database"
menu_choose_server = "Primary server location"
menu_ext4exe = "Use make_ext4fs.exe"
menu_zip_compression = "ROM zip compression level"
menu_zip_compression2 = "Enter the desired zip compression level "
menu_tools_update = "The update will complete on restart"
menu_offline_auth = "Offline Authorization Menu"
menu_offline_renew = "Renew offline authorization"
menu_offline_enable = "Enable/Disable offline authorization"
menu_renew_now = "Renew now"
auth_reset = "Offline authorization has been enabled/renewed. The kitchen needs to restart."
auth_reset2 = "Internet access is required for the first restart."
auth_max_days = "Maximum Offline Authorization Days: "
auth_expired = "Offline authorization session has expired."
support_create = "Creating support.zip ..."
support_finish = "Support zip has been created in your project directory"
support_finish_up = "Support zip has been uploaded"
heapsize_q = "Please enter your custom heapsize in MB. It must be"
heapsize_q2 = "less than your total physical ram:"
heapsize_choose = "What would you like to do?"
heapsize_custom = "Change heapsize for java"
heapsize_reset = "Return to default heapsize detection"
heapsize_num_error = "You must enter a number in MB (Ex. 1024)"
heapsize_error = "Heapsize must be equal to or less than the amount of"
heapsize_error2 = "physical ram installed."
physical_ram = "Physical ram: "
heapsize_auto = "Default"
ask_b = "Ask every time about converting to update-binary script"
ask_s = "Ask every time"
always_b = "Always convert to update-binary script"
always_s = "Always convert"
never_b = "Never convert to update-binary script"
never_s = "Never convert"
metasize = "Short/Long set_metadata updater-script"
metasize_s = "Short"
metasize_l = "Long"
metasize_q = "Which set_metadata updater-script length should we use?"
brotli_q = "Would you like to use brotli compression (dat.br)?"
brotli_level = "Enter the desired brotli compression level "
brotli_menu = "sparse_dat brotli compression (dat.br)"

# Asserts
menu_add_assert = "Add/Remove Device"
menu_asserts_custom = "Add Custom assert"
menu_asserts_remove = "Remove asserts from ROM"
menu_asserts_reset = "Reset asserts to default"
asserts_no_assert = "There is no assert to ammend."
asserts_current = "CURRENT DEVICE ASSERTS: "
asserts_enter = "Device asserts allow/deny the flashing of ROMs. If you"
asserts_enter2 = "allow a ROM to be flashed on the wrong device it can"
asserts_enter3 = "have serious consequences. You have been warned :)"
asserts_enter4 = "Please enter the comma separated device asserts. The"
asserts_enter5 = "current device should already be in the list but make"
asserts_enter6 = "sure it is. Press ENTER when finished."
asserts_prep = "Preparing device asserts ..."
asserts_type = "Type your custom assert below. Press ENTER when finished."
asserts_cust_error = "Syntax must be "
asserts_prep_cust = "Preparing custom assert ..."

# Extra Directory
menu_data = "/data/app"
menu_cust_dir = "Custom"
menu_cctr = "Not active"
extra_data_added = "/data/app support has been added. Place apps in:"
extra_already_data = "You already have /data/app support."
extra_already_data2 = "The /data directory in your project will remain."
extra_already_data3 = "Should we remove it?  y/n"
extra_data_rem = "/data/app support has been removed"
extra_cust_name = "Type the name of the custom directory, then press ENTER."
extra_cust_loc = "Where should the custom directory be flashed?"
extra_cust_name_q = " will be included in your ROM. Should it be flashed to a partition?  y/n"
extra_cust_setup = "Setting up "
extra_cust_add = "support has been added"
extra_data = "Data perm type:"
extra_data_q = "Would you like to add /data/app support?  y/n  "
extra_data_perm = "Please choose /data perm type: "
extra_cust_already = " already exists."

# Selection
select = "Make your selection:  "
select_enter = "Make your selection and press ENTER:  "

# Notices
example = "EXAMPLE:"
warning = "WARNING:"
notice = "NOTICE:"
missing = "MISSING FILES:"
current = "CURRENT"
expires = "EXPIRES: "
error = "ERROR:"
success = "SUCCESS:"
error_mess = "Something went wrong."

# Press ENTER
enter_rom_tools = "Press ENTER to return to ROM Tools menu"
enter_continue = "Press ENTER to continue"
enter_main_menu = "Press ENTER to return to the Main Menu"
enter_boot_menu = "Press ENTER to return to the Boot/Recovery Tools menu"
enter_build_menu = "Press ENTER to return to the Build Menu"
enter_change_perm_menu = "Press ENTER to return to Change Perm menu"
enter_debloat_menu = "Press ENTER to return to the Debloat Menu"
enter_extra_dir_menu = "Press ENTER to return to Extra Directory Menu"
enter_cho_another_detection = "Press ENTER to choose another detection method"
enter_ready = "Press ENTER when ready"
enter_kitchen_updater = "Press ENTER to return to Kitchen updater"
enter_misc_tools_menu = "Press ENTER to return to the Misc Tools menu"
enter_heapsize_menu = "Press ENTER to return to the heapsize menu"
enter_continue_extracting = "Press ENTER to continue extracting"
enter_try_again = "Press ENTER to try again"
enter_root_menu = "Press ENTER to return to the Root Menu"
enter_plug_menu = "Press ENTER to return to the Plugin Manager"
enter_exit = "Press ENTER to exit"

# Perm Type
perm_title = "Change/Choose Perm Menu"
perm_set_metadata_cur = "set_metadata"
perm_set_metadata = "set_metadata (KitKat and Higher)"
perm_set_perm = "set_perm (JellyBean and lower)"
perm_sparse = "Sparse dat"
perm_sparse_red = "Sparse dat (not supported on this device)"
perm_raw_img = "raw_img"
perm_check_symlinks = "Checking symlinks ..."
perm_set_metadata_error = "This ROM is NOT KitKat or higher"
perm_set_perm_error = "This ROM is NOT JellyBean or lower"
perm_changing_perm = "Changing perm type ..."
perm_which = "Which perm type would you like to use?"

# Delete Project
delete_has_been = " has been deleted."
delete_q = "will be deleted. Continue?  y/n"

# Deodex
deodex_copy_frame_prop = "You must copy the framework directory and build.prop"
deodex_copy_frame_prop2 = "from your ROM into "
deodex_no_odex = "There are no odex files in this rom."
deodex_no_boot_oat = "There is no boot.oat in this rom. It cannot be deodexed."
deodex_no_plat = "Deodex of this API is not supported on this platform"
deodex_no_valgrind = "Please install valgrind, and try again"
deodex_disclaimer = "Deodexing ROMs may or may not work. You may get"
deodex_disclaimer2 = "errors, it may not boot, or both. I am aware of"
deodex_disclaimer3 = "the problems. Unless you know how to fix them,"
deodex_disclaimer4 = "please do not post about it. Thanks :)"
deodex_use_method = "Which deodex method should we use?"
deodex_oat2dex_ver = "Which oat2dex version should we use?"
deodex_oat2dex_official = "Official v0.86"
deodex_oat2dex_latest = "Latest release"
title_cho_oat2dex = "Choose oat2dex:"
title_cho_smali = "Choose smali:"
title_cho_baksmali = "Choose baksmali:"
deodex_no_api = "The Android version could not be detected."
deodex_config_arch = "Configure the arch of your device."
deodex_config_arch2 = "HINT:"
deodex_config_arch3 = "Check the framework directory, you should see"
deodex_config_arch4 = "another directory inside. The name of it should go"
deodex_config_arch5 = "here (ex. arm, arm64, x86)."
deodex_config_arch6 = "If you can't get past this part, check the following:"
deodex_config_arch7 = "1. Make sure you typed the arch variable correctly."
deodex_config_arch8 = "2. Make sure your rom is not already deodexed."
deodex_config_arch9 = "Type the arch of your device and press ENTER."
deodex_extract_txt = "Extracting odex files ..."
deodex_extract = "... Extracting "
deodex_move = "Moving extra apps ..."
deodex_deop = "Deoptimizing boot.oat ..."
deodex_start_app = "Start deodexing /system/app ..."
deodex_start_priv = "Start deodexing /system/priv-app ..."
deodex_start_frame = "Start deodexing /system/framework ..."
deodex_deodexing = "... Deodexing "
deodex_app_already = " is already deodexed ..."
deodex_clean = "Cleaning up ..."
deodex_complete = "Deodexing complete"
deodex_remain = "The following odex files are still in your ROM"
deodex_method = "METHOD:"
deodex_problems = "There were problems deodexing the following"
deodex_problems2 = "and may cause issues if you flash the ROM."
deodex_problems3 = "You have been warned:"
deodex_try_smali = "SUGGESTION: Try smali/baksmali"
deodex_api = "API LEVEL: "
deodex_arch = "ARCH: "
deodex_arch2 = "ARCH2: "
deodex_move_odex = "Moving odex files ..."
deodex_try_anyway = "Would you like to try anyway?  y/n  "
deodex_continue_q = "Would you like to continue deodexing?  y/n  "
deodex_del_meta_inf_q = "Android Nougat uses APK Signature Scheme v2, and"
deodex_del_meta_inf_q2 = "this can cause problems when deodexing. Deleting"
deodex_del_meta_inf_q3 = "META-INF from the apk files should fix this problem."
deodex_del_meta_inf_q4 = "Would you like to delete the META-INF directory from"
deodex_del_meta_inf_q5 = "all the apk files in your ROM?  y/n  "
deodex_del_meta_inf = "Deleting META-INF from apk's ..."
deodex_del_arch = "Would you like to delete the framework directories listed below?  y/n"
deodex_pack_jar = "Packing dex into jar files ..."
deodex_server_disabled = "cdex conversion on the server is currently disabled"
deodex_server_cdex = "Converting cdex on server ..."
deodex_server_error1 = "Upload failed"
deodex_server_error2 = "Moving file to working directory failed"
deodex_server_error3 = "cdex zip extraction failed"
deodex_server_error4 = "dex zip creation failed on server"
deodex_no_dex = "No dex in vdex. Skipping."

# Extract
extract_title = "Extract Menu"
extract_no_files_message = "1) Add a ROM zip, tar/boot.img, system.img/boot.img, or"
extract_no_files_message2 = "   win/boot.win then choose this option."
extract_no_files_message3 = "2) Pull system, vendor, boot, and recovery images from your"
extract_no_files_message4 = "   rooted device OR from custom recovery for extraction."
extract_cho_option = "Choose option to extract images"
extract_cho_option2 = "**If you get an error, you can try the other option**"
extract_cho_option3 = "1) My device is booted to custom recovery (stock will not work)"
extract_cho_option4 = "2) My device is booted to Android (must be rooted)"
extract_plug = "** Plug in your device"
extract_detect_part = "Detecting partition info ..."
extract_detect_part2 = "If you are stuck here, try changing the USB mode on"
extract_detect_part3 = "your device from charging to file transfer (MTP)"
extract_pull_error = "Something went wrong. Most likely you lack permission to"
extract_pull_error2 = "pull images from your device."
extract_pulling = "Pulling "
extract_prep = "Preparing to extract ..."
extract_zip_fail = "This zip does not contain anything the kitchen"
extract_zip_fail2 = "can extract."
extract_zip = "Extracting zip ..."
extract_dat = "Extracting system.new.dat, system.transfer.list, and boot.img ..."
extract_convert_br = "Decompressing dat.br ..."
extract_convert_sys = "Converting to "
extract_img_from_zip = "Extracting images from zip ..."
extract_tar_boot = "Extracting system.ext4.tar.a and boot.img ..."
extract_img = "Extracting images ..."
extract_fail = "Something went wrong with the extraction."
extract_tar_md5 = "Extracting tar.md5 files ..."
extract_chunk = "Extracting sparsechunks and boot.img ..."
extract_pbin = "Extracting payload.bin ..."
extract_multi = "Extracting multi-part system ..."
extract_convert_chunk = "Converting sparse chunks to img files ..."
extract_fix_img = "Fixing "
extract_general = "Extracting to "
extract_check_firm = "Checking firmware package ..."
extract_tgz_fail = "The tgz file does not appear to be"
extract_tgz_fail2 = "official Nexus firmware."
extract_files = "Extracting files ..."
extract_md5_fail = "There is no system.img.ext4 in your tar.md5 file"
extract_xz_fail = "There is no system.img in this xz file"
extract_tar_fail = "Looks like the tar file you have is not from a nandroid backup"
extract_tar = "Extracting name"
extract_extra_extract_q = "Would you like to extract extra partitions (modem.bin, etc.)?  y/n  "
extract_cache_extract_q = "Would you like to extract cache.img?  y/n  "
extract_cache_include_q = "Would you like to include the files from cache.img"
extract_cache_include_q2 = "in your rom?  y/n  "
extract_cache = "Including cache.img files ..."
extract_cache_fail = "There is no csc.zip in your cache.img"
extract_rom_fail = "There was a problem extracting your ROM."
extract_rom_fail_ext4 = "Your img file does not seem to be valid ext4."
extract_cho_part_detect = "Choose partition size detection method for "
extract_adb_shell = "Device through adb shell"
extract_project_dir = "Project directory (BETA): "
extract_manual = "Enter manually"
extract_detect = "Determining partition size for "
extract_beta = "This feature is in BETA. It may not flash properly."
extract_beta2 = "You may get an error like the following:"
extract_beta3 = "blkdiscard failed: Invalid argument"
extract_beta4 = "You can change perms to set_metadata or set_perm to"
extract_beta5 = "avoid using this feature"
extract_manual_bytes = "Enter partition size in bytes for "
extract_detect_fail = " partition size is empty or not numeric. Please try again."
extract_sparse_convert = "Converting sparse img ..."
extract_img_fail = "There is no "
extract_copy_e = "Copying files to "
extract_moved_old_rom = "The following have been moved to:"
extract_q = "Should we extract "
extract_q2 = "to the current project?  y/n  "
extract_extra_extract = "Would you like to extract "
extract_extra_q = "?  y/n  "
extract_extra_include = "Would you like to include the files from "
extract_extra_include_q = " in your rom?  y/n  "
extract_autorom_sudo = "Setting sudo now so AutoROM is not interupted"
extract_use_concat = "Use the concatimg plugin, then extract the system.img"

# by-name
byname_how_to_get_q = "How would you like to get your partition info?"
menu_byname_detect_boot = "Detect by-name from boot/recovery images (recommended)"
menu_byname_detect_device = "Detect by-name from your device"
menu_byname_detect_manual = "Enter by-name manually"
menu_byname_detect_mmc = "Detect mmcblk partitions from recovery.img"
byname_usb_debug = "** Enable usb debugging on your Android device in system settings"
byname_usb_debug2 = "** Plug in your device"
byname_usb_debug_root = "This operation requires root."
byname_usb_debug_root2 = "You may need to agree to allow root on your device."
byname_error_device = "by-name could not be detected from your device."
byname_error_device2 = "Try detecting mmc partitions from recovery.img"
byname_no_boot = "Please copy a boot.img, recovery.img, or kernel.elf to the"
byname_no_boot2 = "project directory and try again."
byname_which_img_q = "Which image should we use?"
byname_detect = "Detecting by-name from "
byname_no_files = "You need a boot.img, recovery.img, or kernel.elf for this process."
byname_boot_fail = "by-name could not be detected."
byname_try_recovery = "Try detecting mmc partitions from recovery.img"
byname_detect_manual = "Please enter your by-name directory and press ENTER"
byname_no_byname = "by-name directory is empty."
byname_create_mmc = "Creating mmc from recovery.img ..."
byname_need_recovery = "You need a recovery.img for this process."
byname_no_mmc = "The kitchen can't find the mmc blocks."
byname_recovery_fail = "mmc could not be detected from the recovery.img."
byname_try_boot = "Try detecting by-name partitions from boot.img"

# Signature
sig_info = "The answer to this question will show when flashing"
sig_info2 = "the zip and will be converted into the zip name when"
sig_info3 = "the zip is built."
sig_info_q = "What is the name of your zip?"
sig_info_error = "Do not use / in the zip name"
donate_sig_cust = "This one will show below the zip name when flashing where"
donate_sig_cust2 = "the standard version said Built with SuperR's Kitchen."
donate_sig_q = "What is your signature?"

# Zip devices
zipdev_info = "This option will zip all new device files to share."
zipdev_building = "Building devices zip ..."
zipdev_uploading = "Uploading to server ..."
zipdev_finished = "The devices zip has been created:"
zipdev_upload = "Would you like to upload now so the new files can be"
zipdev_upload2 = "added to the database for others to use?  y/n"
support_upload = "Would you like to upload your support zip now?  y/n"
xdauser_q = "What is your XDA username (leave empty if you don't have one) ?"
zipdev_no_new = "There are no new devices in the devices directory."

# Kitchen updater
update_check_kitchen = "Checking for updates ..."
update_down = "The file server must be down temporarily."
update_down2 = "Please try again later."
update_update_avail = "An update is available!"
update_update_cv = "CURRENT VERSION: "
update_update_nv = "NEW VERSION: "
update_update_now = "Update now"
update_update_view = "View changelog"
update_changelog = "Changelog (last 3 versions):"
update_updating = "Updating ..."
update_finished = "SuperR's Kitchen has been updated and needs to restart."
update_already = "SuperR's Kitchen is already up to date"
update_check_launcher = "Checking for Kitchen Launcher updates ..."
update_launcher_avail = "Launcher update available"
update_launcher_cv = "CURRENT VERSION:"
update_launcher_nv = "NEW VERSION:"
update_launcher_finished = "Installer/Launcher has been updated"
update_problem_download = "There was a problem downloading the update."
update_no_internet = "The Kitchen could not detect an internet connection."
update_fail = "There was a problem updating. Try a"
update_fail2 = "fresh install."
update_fail3 = "Sorry for the trouble."
update_q = "Would you like to update now?  y/n  "
update_auto_q = "Do you want to check for updates when the kitchen starts?  y/n  "
update_auto_toggle = "Check for updates at startup"
update_cred_fail = "Your credentials were not found in the database. You"
update_cred_fail2 = "can update or download the latest version after you"
update_cred_fail3 = "are registered and approved."
update_reg_address = "https://sr-code.com/reg.php"
update_verify = "Verifying file checksums ..."
update_local = "Would you like to install the local update zip?  y/n"
update_latest_version = "is not the latest version. The latest version is"
update_win_final = "This is the final release of the native Windows kitchen."

# New Project
new_q = "Enter new project name (spaces will be replaced with _): "
new_already = "You already have a project with that name"

# Plugin
donate_plugin_cho = "Choose Plugin to Run:"
donate_plugin_install_cho = "Choose Plugin to Install:"
donate_plugin_delete_cho = "Choose Plugin to Delete:"
donate_plugin_error = "Plugin scripts must be in a directory named the same"
donate_plugin_error2 = "as the plugin script."
donate_plugin_server = "Looks like the plugin server is down. Please try again later"
donate_plugin_none = "There are no new plugins to install"
donate_plugin_reinstall_q = "Cannot be checked for updates because it was installed before"
donate_plugin_reinstall_q2 = "the update system."
donate_plugin_reinstall_q3 = "Would you like to reinstall now?  y/n"
donate_plugin_crash = "There was a crash in plugin: "
donate_plugin_crash2 = "Check the plugin.log for details."
donate_plugin_incompat = "Plugin not compatible with this system."

# Sign
sign_ram_check = "Checking ram ..."
sign_no_ram = "You may not have enough ram to sign this zip."
sign_signing = "Signing "
sign_signed = "has been created. Enjoy!"
sign_fail = "Something went wrong with the signing."
sign_q = "Would you like to sign the zip?  y/n  "

# Build img
img_add = "Adding "
img_flash_fail = "The flashable will not work because there"
img_flash_fail2 = "is no partition info for "
img_create_dat = "Creating sparse dat image for "
img_create_symlinks = "Creating symlinks for "
img_create_raw = "Creating "
img_fail = "Something went wrong building the image."
img_fail_size = "Could not determine the partition size."
img_fail_fit = "build failed. Directory will not fit:"
img_fail_log = "build failed. Check the img_build.log for details."
img_dir_open = "Make sure the system directory is not open in"
img_dir_open2 = "your file manager or anywhere else and try again."
img_flash_failB = "The flashable will not work because there is no"
img_flash_failB2 = "partition info. Please create a device directory or enter the"
img_flash_failB3 = "info manually after the zip is created"
img_sparse_q = "What type of system.img should we create?"

# Language
reset_language = "Language has been reset, and the kitchen needs to restart."
lang_added = "New English language elements have been added to "
lang_translate = "Make sure you translate them."

# Tools
tools_dl = "Downloading "
tools_dl_failed = "The tools download failed:"
tools_dl_install_failed = "The tools download/install failed."
tools_dl_device_failed = "Unable to download the device database at this time."
tools_dl_device_failed2 = "You can use Misc Tools > Update device database later"
tools_dl_device_failed3 = "to get the latest version"
wintools_dl = "(approximately 17MB download)"
lintools_dl = "(approximately 24MB download)"
tools_need = "You need tools to continue."
tools_dl_install = "Downloading/Installing now ..."
tools_dl_q = "Would you like to download/install them now?  y/n  "

#Example Plugin
plug_example_text = " Add more plugins to "
