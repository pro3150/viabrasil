const add_item = () => {
    form_div_items = document.querySelector("#checklist_template_items");    
    amount_items = form_div_items.childElementCount;
    order = amount_items / 2; // 2 inputs per item

    input_item_order = document.createElement("input");
    input_item_order.setAttribute("type", "hidden");
    input_item_order.setAttribute("name", "checklist_template_item_order");
    input_item_order.setAttribute("value", order);

    input_item = document.createElement("input");
    input_item.setAttribute("type", "text");
    input_item.setAttribute("name", "checklist_template_item");
    input_item.setAttribute("id", order);
    placeholder = "Item " + (order + 1)
    input_item.setAttribute("placeholder", placeholder);

    form_div_items.appendChild(input_item_order)
    form_div_items.appendChild(input_item);
}   