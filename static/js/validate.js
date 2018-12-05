function ensure() {
    if(window.confirm('Are you sure about this?')) {
        return true;
    } else {
        return false;
    }
}

function is_required(field, ErrMsg) {
    with (field) {
        if(value == null || value == "") {
            alert(ErrMsg);
            return false;
        } else {
            return true;
        }
    }
}

function validate(form) {
    with (form) {
        if(is_required(CostName, "Come on, what cost this much?") == false) {
            CostName.focus();
            return false;
        } else if(is_required(CostMoney, "Spend money instead of happiness is not a shame.") == false) {
            CostMoney.focus();
            return false;
        } else {
            return true;
        }
    }
}