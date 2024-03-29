const token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1IiwianRpIjoiOWM5MzU5ODVlNDUwNzk3Y2JkZDEyZjZmYzFkYjE0MzFiM2JkOTc4OGRiN2NjOWJmZTFmZGU5MzQ3N2QwMWY4NjVlY2Q1YjExZDI2YjQyOWMiLCJpYXQiOjE3MTE3MTAwODUuMTU5MTMzLCJuYmYiOjE3MTE3MTAwODUuMTU5MTM1LCJleHAiOjE3MTE3MTcyODUuMTU0NzY3LCJzdWIiOiIyMTA3NjkiLCJzY29wZXMiOltdfQ.gXiLscGMi_ak19Wcy9iCS-rXLaj59Ttju37sRajt9z6yj4Wb81JZIFpUc1Z6gDtva8n1r8XkM2KxYfnFalcNRK2O3-zsLOje7QMsTUPuVjgahV8ToZx6nL7_d-KtWXI1INzgCbVMaQgveTmLowwh71Li4Eg7acUPSBEddzhplkaTDa6yAkfIfMcrO9LdHW4hUKtP6y-e9WZ1SRN52m7Ekw8uGmua00BhHcwJxAjLaixXa8hh3lUocrC9TNfh6so25CZNsQFcBejNj9qTgfcFpIYECP2PYzPRza8YZBOd-lqGxV5VSdVRTiG4TrUBjWTnRDbCTU-LwCzgIzoeNB4HY3DQnXllCrirjsO26EFdF3IrWOiwzT0Ti_UtV1FX2hXxdXzgOXs18t12OxXUPHvDLDI1pDHALk5p-XayJ0ncogV7Ff4ivjUyknvUIQJN5sFIByW7sklixxagsBjSaRwDOtdzREvXsD1UC-Y1n_5m-BT0LlMfwE0fTw3cbybd7Mnwuojexk_9DH_rna7ibiYPQW8wrnMlaVGmJQzZGERQFrnFKlH0EmPPXBgx-rfARM3zQw1DtRYWoYrcftP81gwwo5mNUTEOAochaTRJDPLvwv5XxCr2Jix3jTk3iHSTZCT_EJRvxr0gbRmJYmAN0hyV5UjyjiXXFXUBt2LGLb8pA4Y';

fetch('https://training.digimal.uonbi.ac.ke/api/administrative_unit?subcounty_id=108', {
    headers: {
        'Authorization': `Bearer ${token}`
    }
})
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    if (data.success) {
        const filteredData = data.data.map(item => {
            return {
                village_id: item.village_id,
                village_name: item.village,
                location: item.location,
                sublocation: item.sublocation,
                ward_id: item.ward_id
            };
        });
        console.log(filteredData);
    } else {
        console.error('Request failed with error:', data.error);
    }
})
.catch(error => {
    console.error('There was a problem with the fetch operation:', error);
});
