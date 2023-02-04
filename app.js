const getTrainId = () => {
    fetch(
            `https://indian-railway-irctc.p.rapidapi.com/getTrainId?trainno=1205`, {
                method: "GET",
                headers: {
                    'X-RapidAPI-Key': '90eef254efmsh198653183e39b73p1cae5djsn49fdaeaf61b1',
                    'X-RapidAPI-Host': 'indian-railway-irctc.p.rapidapi.com'
                }
            }
        )
        .then(response => response.json())
        .then(data => {
            return data;
        })
        .catch(err => {
            return err;
        });
};

getTrainId();