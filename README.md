# mp3inodesorter
Python script to sort files so their inodes align with the alphabetic sort of the names

One pesky thing I've noticed a lot in mp3 players is while the names appear in the right order in the file manager, when you go to play the files they do not play in that order.
For instance, a book on tape:
<table>
  <tr><td>part01.mp3</td></tr>
  <tr><td>part02.mp3</td></tr>
  <tr><td>part03.mp3</td></tr>
  <tr><td>part04.mp3</td></tr>
  <tr><td>part05.mp3</td></tr>
 </table>
  
When you play, it might begin with part01.mp3, but jump to part04.mp3.  No matter how you renamed them they kept being played in the wrong order.
The problem is that the mp3 player isn't sorting the filenames, its playing them in the order of the file inode.  With Xray vision we see that:
<table>
  <tr><td>part01.mp3</td><td>inode 220</td></tr>
  <tr><td>part02.mp3</td><td>inode 223</td></tr>
  <tr><td>part03.mp3</td><td>inode 222</td></tr>
  <tr><td>part04.mp3</td><td>inode 221</td></tr>
  <tr><td>part05.mp3</td><td>inode 224</td></tr>
 </table>
  
To fix this, the script copies each file to a .mp3.new file.  Note, a rename doesn't change the inode, but a copy creates a new file hence
a new inode.  Then it deletes the old files and renames the copies back.

<table>
  <tr><td>part01.mp3</td><td>inode 510</td></tr>
  <tr><td>part02.mp3</td><td>inode 511</td></tr>
  <tr><td>part03.mp3</td><td>inode 512</td></tr>
  <tr><td>part04.mp3</td><td>inode 513</td></tr>
  <tr><td>part05.mp3</td><td>inode 514</td></tr>
</table>

So, copy the mp3 you want onto your SD card, make sure the names sort the way you want the files to be, then run this script and when you run the mp3 player they will play in the right order.
