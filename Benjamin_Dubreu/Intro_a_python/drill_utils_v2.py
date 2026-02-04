# C'est le drill_utils updated avec les conditions si jamais les informations ne se trouvent pas dans le fichier json en entrée
# pour éviter d'écraser des données

from typing import Dict


# EXPECTED_KEYS pourrait être utile dans d'autres fonctions,
# et / ou être modifié à l'avenir,
# donc autant le mettre au début
EXPECTED_KEYS = [
    "machine_id",
    "machine_ID",
    "name",
    "location",
    "status",
    "specifications",
    "last_maintenance_date",
    "next_maintenance_due",
    "contact_information",
]


def convert_miles_to_meters(machine: Dict) -> Dict:
    # Vérifications de sécurité
    if "specifications" not in machine:
        return machine

    specs = machine["specifications"]

    # On ne convertit que si les champs en miles existent
    if (
        "depth_capacity_miles" not in specs
        or "drilling_speed_miles_per_day" not in specs
    ):
        return machine

    depth_capacity_miles = specs["depth_capacity_miles"]
    depth_capacity_meters = depth_capacity_miles * 1609
    specs["depth_capacity_meters"] = depth_capacity_meters

    drilling_speed_miles_per_day = specs["drilling_speed_miles_per_day"]
    drilling_speed_meters_per_day = drilling_speed_miles_per_day * 1609
    specs["drilling_speed_meters_per_day"] = drilling_speed_meters_per_day

    del specs["depth_capacity_miles"]
    del specs["drilling_speed_miles_per_day"]

    return machine


def convert_dates(machine: Dict) -> Dict:
    if "last_maintenance_date" in machine:
        last_maintenance_date = machine["last_maintenance_date"]

        if isinstance(last_maintenance_date, str) and "-" in last_maintenance_date:
            machine["last_maintenance_date"] = "/".join(
                last_maintenance_date.split("-")[::-1]
            )

    if "next_maintenance_due" in machine:
        next_maintenance_due = machine["next_maintenance_due"]

        if isinstance(next_maintenance_due, str) and "-" in next_maintenance_due:
            machine["next_maintenance_due"] = "/".join(
                next_maintenance_due.split("-")[::-1]
            )

    return machine


def add_contact_info(machine: Dict) -> Dict:
    # On n’écrase surtout pas si ça existe déjà
    if "contact_information" in machine:
        return machine

    machine["contact_information"] = {
        "operator_company": None,
        "contact_person": None,
        "phone": None,
        "email": None,
    }

    return machine


def format_machine_id(machine: Dict) -> Dict:
    # Le champ peut ne pas exister
    if "machine_id" not in machine:
        return machine

    machine_id = machine["machine_id"]

    # Sécurité si le format n'est pas celui attendu
    if not isinstance(machine_id, str) or "-" not in machine_id:
        return machine

    id_letters, id_number = machine_id.split("-", 1)

    # Sécurité supplémentaire
    if not id_number.isdigit():
        return machine

    id_number_zfilled = id_number.zfill(3)
    machine["machine_id"] = f"{id_letters}-{id_number_zfilled}"

    return machine


def remove_useless_data(dm_dict: Dict) -> Dict:
    for key in list(dm_dict.keys()):
        if key not in EXPECTED_KEYS:
            del dm_dict[key]

    return dm_dict
