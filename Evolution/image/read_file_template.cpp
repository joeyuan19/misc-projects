#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void process(string line) {
    cout << line << "\n";
}

int main(int argc, char *argv[]) {
    cout << argv[1] << "\n";
    ifstream f (argv[1]);
    string line;
    cout << f << "\n";
    while (getline(f,line)) {
        process(line);
    }
    f.close();
    return 0;
}

