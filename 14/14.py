import xml.etree.ElementTree as ET

def get_address_from_tags(tags_dict):
    """
    Собирает адрес из addr:street, addr:housenumber, addr:city (если есть).
    Возвращает строку. Если ничего не найдено, "Unknown address".
    """
    street = tags_dict.get("addr:street", "")
    house  = tags_dict.get("addr:housenumber", "")
    city   = tags_dict.get("addr:city", "")

    parts = []
    if city:
        parts.append(city)
    if street:
        parts.append(street)
    if house:
        parts.append(house)

    if parts:
        return ", ".join(parts)
    else:
        return "Unknown address"

def find_police_stations_in_file(osm_file):
    """
    Ищет полицейские участки (amenity=police) в одном OSM-файле osm_file.
    Возвращает список кортежей: (address, elem_type, elem_id, source_file).
    """
    tree = ET.parse(osm_file)
    root = tree.getroot()

    results = []

    for element in root.findall("./*"):  # ./node, ./way, ./relation и т.д.
        tags_dict = {}
        for tag_elem in element.findall("tag"):
            k = tag_elem.get("k")
            v = tag_elem.get("v")
            if k and v:
                tags_dict[k] = v

        # Если это полицейский участок
        if tags_dict.get("amenity") == "police":
            address_str = get_address_from_tags(tags_dict)
            elem_type = element.tag      # 'node', 'way', 'relation'...
            elem_id   = element.get("id", "?")
            results.append((address_str, elem_type, elem_id, osm_file))

    return results

def main():
    # Два входных файла
    files = ["15.osm", "15_-2.osm"]

    # Парсим оба файла, собираем всё в общий список
    all_police = []
    for f in files:
        stations = find_police_stations_in_file(f)
        all_police.extend(stations)

    # Сортируем общий список по адресу (1-й элемент кортежа)
    all_police.sort(key=lambda x: x[0].lower())

    # Выводим результат
    print("Найдено полицейских участков (общее кол-во):", len(all_police))
    print("Список (отсортирован по адресу):\n")
    for address, el_type, el_id, source_file in all_police:
        print(f"- {address} ({el_type} #{el_id}) из файла: {source_file}")

if __name__ == "__main__":
    main()
