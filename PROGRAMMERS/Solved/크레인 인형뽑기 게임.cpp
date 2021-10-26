// 2019 카카오 개발자 겨울 인턴쉽
// https://programmers.co.kr/learn/courses/30/lessons/64061
// 크레인 인형뽑기 게임

#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int board_size = board.size();
    int size = moves.size();

    stack<int> result;

    for (int i = 0; i < size; i++) {
        int index = moves[i] - 1;
        for (int j = 0; j < board_size; j++) {
            if (board[j][index] != 0) {
                int temp = board[j][index];
                board[j][index] = 0;
                if (!result.empty()) {
                    int top_stack = result.top();
                    if (top_stack == temp) {
                        answer += 2;
                        result.pop();
                    }
                    else
                        result.push(temp);
                }
                else
                    result.push(temp);
                break;
            }
        }
    }
    return answer;
}