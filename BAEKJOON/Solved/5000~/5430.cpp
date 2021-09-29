// 5430 - AC
// Queue, 파싱
// 덱의 개념 사용해야한다

#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main() {
    int test_case;

    cin >> test_case;

    while (test_case > 0) {

        int num;
        int i = 0, digit = 0, total_D = 0;
        bool front = true, err = false;
        string func, input_arr;
        deque<int> num_dequeue;

        cin >> func;
        cin >> num;
        cin.ignore();
        getline(cin, input_arr);

        while (input_arr[i] != '\0') {
            while (input_arr[i] >= '0' && input_arr[i] <= '9') {
                digit *= 10;
                digit += (int(input_arr[i]) + 2) % 10;
                i++;
            }
            if (digit != 0) {
                num_dequeue.push_back(digit);
                digit = 0;
            }
            i++;
        }

        i = 0;
        while (func[i] != '\0') {
            if (func[i] == 'R')
                front = !front;
            else if (func[i] == 'D') {
                total_D++;
                if (num_dequeue.empty()) {
                    cout << "error\n";
                    err = true;
                    break;
                }
                if (front)
                    num_dequeue.pop_front();
                else
                    num_dequeue.pop_back();
            }
            i++;
        }

        i = 0;
        if (!err) {
            cout << "[";
            while (i < num - total_D) {
                if (front) {
                    cout << num_dequeue.front();
                    num_dequeue.pop_front();
                }
                else {
                    cout << num_dequeue.back();
                    num_dequeue.pop_back();
                }
                if (!num_dequeue.empty())
                    cout << ",";
                i++;
            }
            cout << "]\n";
        }
        test_case--;
    }
}