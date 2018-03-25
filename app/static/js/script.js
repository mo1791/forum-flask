const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NjMzMWJmMC1iMGZmLTQyN2MtOTYyOC0zMTFmNGNlM2I5ZmMiLCJleHAiOjE1NTM0Nzg5OTgsImZyZXNoIjpmYWxzZSwiaWF0IjoxNTIxOTQyOTk4LCJ0eXBlIjoiYWNjZXNzIiwibmJmIjoxNTIxOTQyOTk4LCJpZGVudGl0eSI6IjExOWZlMzAxYy0yOGFmLTRjMDQtOWI3Mi1hMmNiODM1M2QwN2UifQ.N5pULXr5vSpJQnlnWqz08NPKRS8--ksQhYb52iPbUKg"

const mixin = {
	methods: {
		getData() {
			const form = document.querySelector("#form")
			const data = new FormData(form)
			const vals = Array.from(data.entries()).reduce((obj, [name, value]) => {
				obj[name] = value
				return obj
			}, {})
			return JSON.stringify(vals)
		}
	},
}