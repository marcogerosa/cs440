class FileInputStream {
   File file;
   int position = 0;
   public int read() {
       if (file.endOfFile() == true) {
           return -1;
       } else {
           position = position + 1;
           readNumber(position);
       }
   }
   int readNumber(int position) {
       // some complicated logic
   }
}


class EndlessFileInputStream extends FileInputStream {
   public int read() {
       if (file.endOfFile() == true) {
           position = 0;
       } else {
           position = position + 1;
           return readNumber(position);
       }
   }
}
