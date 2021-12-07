import unittest
from tts import rooms, generate_reply_message


def generate_cases():
    boiler_plate_inputs = [
        "can you take me to",
        "please take me to",
        "where is",
        "guide me to",
        "show me the way to",
        "how do i get to",
        "can you guide me to",
        "can you take me to",
    ]
    test_cases = []

    for input in boiler_plate_inputs:
        for room in rooms:
            test_case = f"{input} {room}"
            test_cases.append([test_case, room])
    return test_cases


def generate_expected_output(room_name):
    return f"Okay let's head to {room_name}. "


class TTSTest(unittest.TestCase):

    def test_input_cases(self):

        LOG = "log.txt"
        CASE = "cases.txt"
        FAILED = "failed.txt"

        # clearing files
        open(LOG, "w").close()
        open(CASE, "w").close()
        open(FAILED, "w").close()

        log = open(LOG, "a")
        cases = open(CASE, "a")
        fail = open(FAILED, "a")

        passed = 0
        failed = 0
        id = 0

        for test_case in generate_cases():

            test_text = test_case[0]
            room_name = test_case[1]

            try:
                received_output, _ = generate_reply_message(test_text)
            except:
                failed += 1
                fail.write(f"{id}\t{test_text}\n")
                continue

            expected_output = generate_expected_output(room_name)

            try:
                self.assertEqual(received_output, expected_output)
                cases.write(f"{id}\t{test_text}\n")
                log.write(f"{id}\t{received_output}\t{expected_output}\n")
                passed += 1
            except:
                fail.write(f"{id}\t{test_text}\n")
                failed += 1
            id += 1

        log.close()
        cases.close()
        fail.close()

        print(f"PASSED : {passed}")
        print(f"FAILED : {failed}")


if __name__ == "__main__":
    unittest.main()
