class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        --n;

        digits[n] = (++digits[n]) % 10;

        if (digits[n] != 0) {
            return digits;
        } else {
            bool push_front = true;

            for (int i = n - 1; i >= 0; --i) {
                digits[i] = (++digits[i]) % 10;

                if (digits[i] != 0) {
                    push_front = false;
                    break;
                }
            }

            if (push_front) {
                digits.insert(digits.begin(), 1);
            }
        }

        return digits;
    }
};
