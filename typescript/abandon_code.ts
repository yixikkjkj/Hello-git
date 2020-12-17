    // if (typeof column.sorter == 'object' && column.sorter && column.sorter.compare) {
    //   const column_key = (column.dataIndex ?? column.key ?? '') as string;  // 此处隐藏了 ReactText 的属性
    //   if (sort_info[column_key] && sort_info[column_key].order) {
    //     (rlt.sorter as any).multiple = sort_info[column_key].multiple;
    //     rlt.sortOrder = sort_info[column_key].order;
    //   }
    // }
    // const column_key = (column.dataIndex ?? column.key ?? '') as string;  // 此处隐藏了 ReactText 的属性
    // if (sort_keys[column_key] != undefined) {
    //   rlt.sortOrder = sort_keys[column_key].order;
    // }



    // let new_sorters: any = {};
    // const handleSorter = (sorter: SorterResult<any>) => {
    //   const old_info = sort_info[sorter.columnKey || ''];
    //   if (old_info == undefined) {
    //     const multiple_list = [...Object.values(sort_info), ...Object.values(new_sorters)].map((tmp: any) => tmp.multiple);
    //     const next_multiple = multiple_list.length > 0 ? Math.max(...multiple_list) + 1 : 1;
    //     new_sorters[sorter.columnKey || ''] = {
    //       ...sorter,
    //       multiple: next_multiple,
    //     };
    //   } else if (sorter.order != undefined) {
    //     new_sorters[sorter.columnKey || ''] = { ...old_info, ...sorter };
    //   }
    // }
    // if (Array.isArray(sorters)) {
    //   sorters.forEach((sorter) => { handleSorter(sorter) });
    // } else {
    //   handleSorter(sorters);
    //   if (sorters.order == undefined) {
    //     delete sort_info[sorters.columnKey || ''];
    //   }
    //   new_sorters = { ...sort_info, ...new_sorters };
    // }

    // console.log('new sorterssssss', new_sorters);
    // setSortInfo(new_sorters);

    // const handleSorter = (sorter: SorterResult<any>) => {
    //   if (sorter.order == undefined) {
    //     delete sort_keys[sorter.columnKey || ''];
    //     return;
    //   }
    //   const multiple_list = Object.values(sort_keys).map((tmp: any) => tmp.multiple);
    //   const next_multiple = multiple_list.length > 0 ? Math.max(...multiple_list) + 1 : 1;
    //   sort_keys[sorter.columnKey || ''] = {
    //     key: sorter.columnKey,
    //     order: sorter.order,
    //     multiple: next_multiple,
    //   };
    // }

    // if (Array.isArray(sorters)) {
    //   sorters.forEach((sorter) => handleSorter(sorter));
    // } else {
    //   handleSorter(sorters);
    // }

    // console.log('new sortkkekkekek', sort_keys);

    // setSortKeys({ ...sort_keys });
    // setRefresh(!refresh);
