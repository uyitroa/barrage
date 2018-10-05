//
// Created by yuitora . on 05/10/2018.
//

#include "SendMail.h"
#include "SendSMS.h"

int main() {
	bool alert = true;
	SendSMS sms;
	SendMail mail;
	std::string alert_string = "ALERT";

	while (true) {
		if (alert) {
			sms.send(alert_string);
			mail.send(alert_string);
		}
	}
}