## Generated Story 6347165289264377209
* court_request_information{"whichCourt": "\u5fb7\u6e05 \u6cd5\u9662"}
    - slot{"whichCourt": "\u5fb7\u6e05 \u6cd5\u9662"}
    - slot{"whichCourt": "\u5fb7\u6e05\u6cd5\u9662"}
    - slot{"whichCourtLast": "\u5fb7\u6e05\u6cd5\u9662"}
    - action_affirm_court_information
* court_request_information{"whichCourt": "\u5fb7\u6e05 \u6cd5\u9662", "courtAddress": "\u5730\u5740"}
    - slot{"whichCourt": "\u5fb7\u6e05 \u6cd5\u9662"}
    - slot{"detailInfo": "FYDZ"}
    - slot{"detailInfoLast": "FYDZ"}
    - slot{"whichCourt": "\u5fb7\u6e05\u6cd5\u9662"}
    - slot{"whichCourtLast": "\u5fb7\u6e05\u6cd5\u9662"}
    - action_affirm_court_information
    - utter_ask_if_continue
* continue_court_info
    - slot{"detailInfo": null}
    - action_continue_current_court
* continue_court_info{"courtPostcode": "\u90ae\u7f16"}
    - slot{"detailInfo": "YB"}
    - slot{"detailInfoLast": "YB"}
    - action_continue_current_court
    - utter_ask_if_continue
* back_menu
    - export

