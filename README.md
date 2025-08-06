Nama: Samuel Yoel Isliko
NIM: 18024063

PERILAKU PACKAGE pkg_18024063:
Package pkg_18024063 berisikan sebuah node "twist_republisher_node" (TRN) yang berfungsi untuk melanjutkan pesan Twist dari node "twist_command_randomizer" (TCR) ke "movement_reader" (MR). Node TRN memiliki sebuah subscriber ke topic 
/autonomous_vel untuk menerima pesan Twist yang telah dipublish oleh node TCR. Kemudian, node ini memiliki publisher ke due topik lain, yaitu /cmd_type dan /cmd_vel, yang di-subscribe oleh node MR. Pesan yang di-publish ke /cmd_type berjenis 
String dengan tulisan "autonomous" sebagai penanda bahwa pesan tersebut diterima oleh TRN dari topic /autonomous_vel, sedangkan pesan yang di-publish ke /cmd_vel adalah pesan Twist yang diteruskan dari node TCR.
Implementasi package dilakukan dengan Python dalam file autonomous_repub.py.

CARA MENJALANKAN:
1. Buat sebuah workspace
2. Clone repository ms2-tubes1-cakrai17 dan repository github ini ke folder src.
3. Buka terminal 2 terminal dan navigasi ke workspace --> cd {workspace_path}
4. Build terminal dan source workspace
   colcon build --symlink-install
   source install/setup.bash
6. Di terminal 1, jalankan nodes dalam package magang_2025
   ros2 run magang_2025 milestone2.launch.py
8. Di terminal 2, jalankan node dalam pkg_18024063
   ros2 run pkg_18024063 autonomous_repub.py

Node berhasil di-execute ketika keluar pesan berikut:
Twist Republisher Node started. Subscribing to /autonomous_vel...
Republishing to /cmd_vel and /cmd_type...

Saat pesan Twist berhasil diterima node MR, pesan berikut akan keluar:
Republished Twist and String from autonomous command.
