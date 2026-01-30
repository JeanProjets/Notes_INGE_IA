from typing import Dict


def convert_miles_to_meters(machine: Dict) -> Dict:
    specs = machine["specifications"]  # specs: short for specifications

    depth_capacity_miles = specs["depth_capacity_miles"]
    depth_capacity_meters = depth_capacity_miles * 1609  # 1 mile = 1.609km = 1609m
    specs["depth_capacity_meters"] = depth_capacity_meters

    drilling_speed_miles_per_day = specs["drilling_speed_miles_per_day"]
    drilling_speed_meters_per_day = drilling_speed_miles_per_day * 1609
    specs["drilling_speed_meters_per_day"] = drilling_speed_meters_per_day

    # remove fields with miles
    del specs["depth_capacity_miles"]
    del specs["drilling_speed_miles_per_day"]

    return machine


def convert_dates(machine: Dict) -> Dict:
    last_maintenance_date = machine["last_maintenance_date"]
    machine["last_maintenance_date"] = "/".join(last_maintenance_date.split("-")[::-1])

    next_maintenance_due = machine["next_maintenance_due"]
    machine["next_maintenance_due"] = "/".join(next_maintenance_due.split("-")[::-1])

    return machine


def add_contact_info(machine: Dict) -> Dict:
    machine["contact_information"] = {
        "operator_company": None,
        "contact_person": None,
        "phone": None,
        "email": None,
    }

    return machine


def format_machine_id(machine: Dict) -> Dict:
    id_letters, id_number = machine["machine_id"].split("-")

    id_number_zfilled = id_number.zfill(3)
    machine_id = f"{id_letters}-{id_number_zfilled}"
    machine["machine_id"] = machine_id

    return machine
