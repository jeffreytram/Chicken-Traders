
function loadStats(transactionDataset, netWorthDataset, npcCount, distTravel ) {
    function getFavoriteItem(dataset) {
        let itemsPurchased = dataset.filter(entry => entry.category === "trade" && entry.transaction_type === "expenses");
        let itemMap = new Map();
        for (let i = 0; i < itemsPurchased.length; i++) {
            let currItemName = itemsPurchased[i].item;
            if (itemMap.has(currItemName)) {
                //item exists
                itemMap.set(currItemName, itemMap.get(currItemName) + 1);
            } else {
                //item doesnt exist yet
                itemMap.set(currItemName, 1);
            }
        }
        let itemIt = itemMap.keys();
        let curr = itemIt.next();
        let max = { name: "None", count: 0 };
        while (!curr.done) {
            if (itemMap.get(curr.value) > max.count) {
                max.name = curr.value;
                max.count = itemMap.get(curr.value);
            }
            curr = itemIt.next();
        }
        document.getElementById('fav-item').innerHTML = max.name;
    }

    function getRepairsPurchased(dataset) {
        let repairsPurchased = dataset.filter(entry => entry.item === "repairs");
        document.getElementById('num-repairs').innerHTML = repairsPurchased.length * 10 + " health";
    }

    function getFuelPurchased(dataset) {
        let fuelPurchases = dataset.filter(entry => entry.item === "fuel");
        document.getElementById('num-fuel').innerHTML = fuelPurchases.length * 50 + " kgs";
    }

    function getTotalNumberItemsSold(dataset) {
        let items = dataset.filter(entry => entry.category === "trade" && entry.transaction_type === "earnings");
        document.getElementById('num-sold').innerHTML = items.length;
    }

    function getNumberTransactions(dataset) {
        document.getElementById('num-transactions').innerHTML = dataset.length;
    }

    function getTotalNumberItemsPurchased(dataset) {
        let items = dataset.filter(entry => entry.category === "trade" && entry.transaction_type === "expenses");
        document.getElementById('num-purchased').innerHTML = items.length;
    }

    function getDistanceTraveled(dist) {
        document.getElementById('dist-traveled').innerHTML = dist.toFixed(1) + " km";
    }

    function getNpcCount(npcCount) {
        document.getElementById('num-npc').innerHTML = npcCount;
    }

    function loadEarningsChart(dataset) {
        let earnings = dataset.filter(entry => entry.transaction_type === "earnings");
        let categories = [
            { name: "trade", total: 0, color: "green" },
            { name: "loot", total: 0, color: "orange" },
            { name: "collection", total: 0, color: "red" }
        ];
        let total = 0;
        earnings.forEach(function (entry, i) {
            total += entry.price;
            if (entry.category === "trade") {
                categories[0].total += entry.price;
            } else if (entry.category === "loot") {
                categories[1].total += entry.price;
            } else if (entry.category === "collection") {
                categories[2].total += entry.price;
            }
        });

        const width = 300;
        const height = 150;
        const radius = Math.min(width, 2 * height) / 2;
        const thickness = 30;

        let pie = d3.pie()
            .value(function (entry) {
                return entry.total;
            })
            .sort(null)
            .startAngle(-90 * (Math.PI / 180))
            .endAngle(90 * (Math.PI / 180));

        let arc = d3.arc()
            .outerRadius(radius)
            .innerRadius(radius - thickness)

        let translation = (x, y) => `translate(${x}, ${y})`;

        let svg = d3.select('#earnings')
            .attr('width', width)
            .attr('height', height)
            .attr('viewBox', [0, 0, width, height])
            .attr('preserveAspectRatio', 'xMidYMid meet')
            .attr('class', 'half-donut')
            .append('g')
            .attr('transform', translation(width / 2, height));

        const div = d3.select('body').append('div')
            .attr('class', 'tooltip')
            .style('opacity', 0);

        svg.selectAll('path')
            .data(pie(categories))
            .enter()
            .append('path')
            .attr('d', arc)
            .attr('fill', (entry) => entry.data.color)
            .on('mouseover', (entry) => {
                let percentage = entry.data.total * 100 / total;
                div.html(`${percentage.toFixed(1)}%: ${entry.data.name}<br>$${entry.data.total}`)
                    .style('opacity', 0.85)
                    .style('font-weight', 'bold')
                    .style('left', `${d3.event.pageX - 45}px`)
                    .style('top', `${d3.event.pageY - 40}px`);
            })
            .on('mouseout', () => {
                div.style('opacity', 0);
            });

        svg.append('text')
            .text('$' + total)
            .attr('dy', '-3rem')
            .attr('class', 'label')
            .attr('text-anchor', 'middle');

        svg.append('text')
            .text('earnings')
            .attr('dy', '-1rem')
            .attr('class', 'label')
            .attr('text-anchor', 'middle');
    }

    function loadExpensesChart(dataset) {
        let expenses = dataset.filter(entry => entry.transaction_type == "expenses");
        let categories = [
            { name: "trade", total: 0, color: "green" },
            { name: "fees", total: 0, color: "yellow" },
            { name: "fuel", total: 0, color: "red" },
            { name: "repairs", total: 0, color: "blue" }
        ];
        let total = 0;
        expenses.forEach(function (entry, i) {
            total += entry.price;
            if (entry.category === "trade") {
                categories[0].total += entry.price;
            } else if (entry.category === "fees") {
                categories[1].total += entry.price;
            } else if (entry.category === "fuel") {
                categories[2].total += entry.price;
            } else if (entry.category === "repairs") {
                categories[3].total += entry.price;
            }
        });

        const width = 300;
        const height = 150;
        const radius = Math.min(width, 2 * height) / 2;
        const thickness = 30;

        let pie = d3.pie()
            .value(function (entry) {
                return entry.total;
            })
            .sort(null)
            .startAngle(-90 * (Math.PI / 180))
            .endAngle(90 * (Math.PI / 180));

        let arc = d3.arc()
            .outerRadius(radius)
            .innerRadius(radius - thickness)

        let translation = (x, y) => `translate(${x}, ${y})`;

        let svg = d3.select('#expenses')
            .attr('width', width)
            .attr('height', height)
            .attr('viewBox', [0, 0, width, height])
            .attr('preserveAspectRatio', 'xMidYMid meet')
            .attr('class', 'half-donut')
            .append('g')
            .attr('transform', translation(width / 2, height));

        const div = d3.select('body').append('div')
            .attr('class', 'tooltip')
            .style('opacity', 0);

        svg.selectAll('path')
            .data(pie(categories))
            .enter()
            .append('path')
            .attr('d', arc)
            .attr('fill', (entry) => entry.data.color)
            .on('mouseover', (entry) => {
                let percentage = entry.data.total * 100 / total;
                div.html(`${percentage.toFixed(1)}%: ${entry.data.name}<br>$${entry.data.total}`)
                    .style('opacity', 0.85)
                    .style('font-weight', 'bold')
                    .style('left', `${d3.event.pageX - 45}px`)
                    .style('top', `${d3.event.pageY - 40}px`);
            })
            .on('mouseout', () => {
                div.style('opacity', 0);
            });

        svg.append('text')
            .text('$' + total)
            .attr('dy', '-3rem')
            .attr('class', 'label')
            .attr('text-anchor', 'middle');

        svg.append('text')
            .text('expenses')
            .attr('dy', '-1rem')
            .attr('class', 'label')
            .attr('text-anchor', 'middle');
    }

    function loadNetWorthChart(dataset) {
        const width = 540;
        const height = 400;

        //getting svg
        const svg = d3.select('#net-worth')
            .attr('viewBox', `0 0 ${width} ${height}`);

        const render = data => {
            const xValue = d => d.day;
            const yValue = d => d.amount;
            const margin = { top: 30, right: 20, bottom: 60, left: 100 };
            const innerWidth = width - margin.left - margin.right;
            const innerHeight = height - margin.top - margin.bottom;

            const xScale = d3.scaleLinear()
                .domain([0, (dataset.length - 1) / 12])
                .range([0, innerWidth]);

            const yScale = d3.scaleLinear()
                .domain([0, d3.max(dataset, yValue)])
                .range([innerHeight, 0]);

            const g = svg.append('g')
                .attr('transform', `translate(${margin.left}, ${margin.top})`);

            //x axis
            const xAxis = d3.axisBottom(xScale)
                .ticks(4);
            const xAxisG = g.append('g').call(xAxis)
                .attr('transform', `translate(0, ${innerHeight})`);
            xAxisG.append('text')
                .attr('x', innerWidth / 2)
                .attr('y', 50)
                .attr('fill', 'black')
                .attr('font-weight', 'bold')
                .text('Day');

            //y axis
            const yAxis = d3.axisLeft(yScale)
            const yAxisG = g.append('g').call(yAxis)
            yAxisG.append('text')
                .attr('x', -50)
                .attr('y', innerHeight / 2)
                .attr('fill', 'black')
                .attr('font-weight', 'bold')
                .text('Credits');

            g.append('text')
                .attr('x', innerWidth / 2)
                .attr('y', 0)
                .attr('fill', 'black')
                .text('Estimated Net Worth Over Time')
                .attr('text-anchor', 'middle');

            //Line Graph
            g.append('path').datum(dataset)
                .attr('fill', 'none')
                .attr('stroke', 'steelblue')
                .attr('stroke-width', 1.5)
                .attr('d', d3.line()
                    .x(d => xScale(xValue(d)))
                    .y(d => yScale(yValue(d)))
                );
        };
        render(dataset);
    }

    loadEarningsChart(transactionDataset);
    loadExpensesChart(transactionDataset);
    loadNetWorthChart(netWorthDataset);
    
    getTotalNumberItemsPurchased(transactionDataset);
    getTotalNumberItemsSold(transactionDataset);
    getNumberTransactions(transactionDataset);
    getFuelPurchased(transactionDataset);
    getRepairsPurchased(transactionDataset);
    getFavoriteItem(transactionDataset);
    getNpcCount(npcCount);
    getDistanceTraveled(distTravel);
}