#include <iostream>
#include <fstream>

int main( int argc, char *argv[] ){

  std::ifstream ifs (argv[1], std::ifstream::in);
  std::ifstream fileList (argv[3], std::ifstream::in);  
  std::ofstream ofs; ofs.open(argv[2]);

  std::string line;
  getline(ifs,line);
  ofs << line << "\n";
  
  std::string file;
  
  int pos;
  while( getline(ifs,line) ) {
    if( line.find("fileNames") != std::string::npos ){
       pos = line.find("(");
       while( getline(fileList,file) ){
          std::cout << file << std::endl;
          line.insert(pos+1,file);
          std::cout << line << std::endl;
	  ofs << "                  " << line << "\n";
	  line = "";
	  pos = -1;
       } 
    }
    ofs << line << "\n";    
  }

  ifs.close();
  fileList.close();
  ofs.close();

  return 0;

}
